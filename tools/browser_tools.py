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
        """Navigate to a URL and return the resulting page title."""
        self.session.url = url
        title = self.session.driver.title
        return f"Navigated to {url}. Page title: '{title}'"

    def browser_click(self, selector: str) -> str:
        """Click an element by CSS selector or XPath."""
        from selenium.webdriver.common.by import By
        driver = self.session.driver
        # Try CSS first, fall back to XPath
        try:
            el = driver.find_element(By.CSS_SELECTOR, selector)
        except Exception:
            el = driver.find_element(By.XPATH, selector)
        el.click()
        return f"Clicked element: {selector}"

    def browser_type(self, selector: str, text: str) -> str:
        """Type text into an input field."""
        from selenium.webdriver.common.by import By
        driver = self.session.driver
        el = driver.find_element(By.CSS_SELECTOR, selector)
        el.clear()
        el.send_keys(text)
        return f"Typed '{text}' into {selector}"

    def browser_get_text(self, selector: Optional[str] = None) -> str:
        """Return visible text from the page or a specific element."""
        from selenium.webdriver.common.by import By
        driver = self.session.driver
        if selector:
            el = driver.find_element(By.CSS_SELECTOR, selector)
            return el.text
        return driver.find_element(By.TAG_NAME, "body").text

    def browser_screenshot(self, filename: Optional[str] = None) -> str:
        """Save a screenshot and return the file path."""
        import os
        import time
        name = filename or f"screenshot_{int(time.time())}"
        path = os.path.join("screenshots", f"{name}.png")
        os.makedirs("screenshots", exist_ok=True)
        self.session.driver.save_screenshot(path)
        return f"Screenshot saved to {path}"

    def dispatch(self, tool_name: str, args: dict) -> str:
        """Dispatch a tool call by name to the appropriate method."""
        method = getattr(self, tool_name, None)
        if method is None:
            raise ValueError(f"Unknown browser tool: {tool_name}")
        return method(**args)
