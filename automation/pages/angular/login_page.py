from playwright.sync_api import Page
from typing import Optional


class LoginPage:
    """Page Object Model for the login page."""
    
    def __init__(self, page: Page):
        """
        Initialize the login page.
        
        Args:
            page: Playwright page instance
        """
        self.page = page
        self.url = "http://localhost:3000/"
        
        # Selectors
        self.login_link = "a:has-text('Iniciar sesión')"  # Link with text "Iniciar sesión"
        self.email_input = "#email"  # Email field by ID
        self.password_input = "#password"  # Password field by ID
        self.submit_button = "button[type='submit']"  # Submit button
    
    def navigate(self) -> None:
        """Navigate to the application base URL."""
        self.page.goto(self.url)
    
    def click_login_link(self) -> None:
        """Click on the 'Iniciar sesión' link or button."""
        self.page.click(self.login_link)
    
    def fill_email(self, email: str) -> None:
        """
        Fill the email field.
        
        Args:
            email: Email address to enter
        """
        self.page.fill(self.email_input, email)
    
    def fill_password(self, password: str) -> None:
        """
        Fill the password field.
        
        Args:
            password: Password to enter
        """
        self.page.fill(self.password_input, password)
    
    def click_submit(self) -> None:
        """Click on the login form submit button."""
        self.page.click(self.submit_button)
    
    def login(self, email: str, password: str) -> None:
        """
        Perform complete login flow.
        
        Args:
            email: Email address
            password: Password
        """
        self.navigate()
        self.click_login_link()
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()
    
    def is_logged_in(self) -> bool:
        """
        Verify if the user has logged in successfully.
        
        Returns:
            True if logged in, False otherwise
        """
        # You can adjust this according to your needs
        # For example, verify if a specific element is visible
        try:
            # Wait for the login form to disappear
            self.page.wait_for_selector(self.email_input, state="hidden", timeout=5000)
            return True
        except:
            return False
