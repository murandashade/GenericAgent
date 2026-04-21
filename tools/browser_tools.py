"""Browser interaction tools for GenericAgent using TMWebDriver."""

from TMWebDriver import Session
from typing import Optional

# Tool schemas to be loaded by agentmain.py
TOOL_SCHEMAS = [
    {
        "name": "browser_navigate",
        "description": "Navigate the browser to a given URL.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to navigate to."
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "browser_click",
        "description": "Click an element on the page identified by a CSS selector or XPath.",
        "parameters": {
            "type": "object",
            "properties": {
                "selector": {
                    "type": "string",
                    "description": "CSS selector or XPath of the element to click."
                }
            },
            "required": ["selector"]
        }
    },
    {
        "name": "browser_type",
        "description": "Type text into an input field identified by a CSS selector.",
        "parameters": {
            "type": "object",
            "properties": {
                "selector": {
                    "type": "string",
                    "description": "CSS selector of the input element."
                },
                "text": {
                    "type": "string",
                    "description": "Text to type into the field."
                }
            },
            "required": ["selector", "text"]
        }
    },
    {
        "name": "browser_get_text",
        "description": "Get the visible text content of the current page or a specific element.",
        "parameters": {
            "type": "object",
            "properties": {
                "selector": {
                    "type": "string",
                    "description": "Optional CSS selector to scope text extraction. If omitted, returns full page text."
                }
            },
            "required": []
        }
    },
    {
        "name": "browser_screenshot",
        "description": "Take a screenshot of the current browser state and return the file path.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Optional filename to save the screenshot as (without extension)."
                }
            },
            "required": []
        }
    }
]


class BrowserTools:
    """Wraps TMWebDriver session to provide tool-callable browser actions."""

    def __init__(self, session: Session):
        self.session = session

    def browser_navigate(self, url: str) -> str:
        """Navigate to a URL and return the resulting page title.

        Note: prepends https:// if no scheme is provided, which saves the agent
        from failing on bare domain strings like 'example.com'.
        """
        # Auto-prepend scheme so bare domains don't cause a navigation error
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.session.url = url
        title = self.session.driver.title
        return f"Navigated to {url}. Page title: {title}"
