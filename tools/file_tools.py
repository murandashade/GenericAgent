"""File system tools for GenericAgent.

Provides read, write, and directory listing capabilities
that the agent can use to interact with the local filesystem.
"""

import os
import json
from pathlib import Path


class FileTools:
    """Tools for reading and writing files on the local filesystem."""

    def __init__(self, working_dir: str = "."):
        """
        Args:
            working_dir: Root directory the agent is allowed to operate within.
                         Paths outside this directory will be rejected.
        """
        self.working_dir = Path(working_dir).resolve()

    def _safe_path(self, path: str) -> Path:
        """Resolve and validate that a path stays within working_dir."""
        resolved = (self.working_dir / path).resolve()
        # Use os.path.commonpath for a more robust containment check
        if os.path.commonpath([str(resolved), str(self.working_dir)]) != str(self.working_dir):
            raise PermissionError(
                f"Access denied: '{path}' resolves outside the working directory."
            )
        return resolved

    def file_read(self, path: str) -> str:
        """Read the contents of a file.

        Args:
            path: Relative path to the file.

        Returns:
            The file contents as a string.
        """
        target = self._safe_path(path)
        if not target.exists():
            return f"Error: File '{path}' does not exist."
        if not target.is_file():
            return f"Error: '{path}' is not a file."
        try:
            return target.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file: {e}"

    def file_write(self, path: str, content: str, overwrite: bool = True) -> str:
        """Write content to a file, creating it (and parent dirs) if needed.

        Args:
            path: Relative path to the file.
            content: Text content to write.
            overwrite: If False, refuse to overwrite an existing file.
                       Defaults to True.

        Returns:
            A success or error message.
        """
        target = self._safe_path(path)
        # Guard against accidentally clobbering existing files when overwrite=False
        if not overwrite and target.exists():
            return f"Error: '{path}' already exists and overwrite is disabled."
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            return f"Successfully wrote {len(content)} characters to '{path}'."
        except Exception as e:
            return f"Error writing file: {e}"

    def file_append(self, path: str, content: str) -> str:
        """Append content to an existing file (or create it).

        Args:
            path: Relative path to the file.
            content: Text content to append.

        Returns:
            A success or error message.
        """
        target = self._safe_path(path)
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("a", encoding="utf-8") as f:
                f.write(content)
            return f"Successfully appended {len(content)} characters to '{path}'."
        except Exception as e:
            return f"Error appending to file: {e}"

    def list_directory(self, 