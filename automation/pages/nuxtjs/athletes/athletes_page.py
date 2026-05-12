from playwright.sync_api import Page


class AthletesPage:
    """Page Object Model for the athletes section after login."""
    
    def __init__(self, page: Page):
        """
        Initialize the athletes page.
        
        Args:
            page: Playwright page instance
        """
        self.page = page
        
        # Selectors for athletes section
        self.athletes_section = "h2:has-text('deportistas')"  # H2 with text "deportistas"
        self.start_now_link = "a:has-text('comenzar ahora')"  # Link with text "comenzar ahora"
    
    def click_athletes_section(self) -> None:
        """Click on the h2 element with text 'deportistas'."""
        self.page.click(self.athletes_section)
    
    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the current view."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    def click_start_now(self) -> None:
        """Click on the 'comenzar ahora' link."""
        self.page.click(self.start_now_link)
    
    def complete_athletes_flow(self) -> None:
        """
        Complete the full athletes flow:
        - Click on athletes section
        - Scroll to bottom
        - Click on 'comenzar ahora'
        """
        self.click_athletes_section()
        self.page.wait_for_timeout(1000)  # Wait for any animations/transitions
        self.scroll_to_bottom()
        self.page.wait_for_timeout(1000)  # Wait for scroll to complete
        self.click_start_now()
