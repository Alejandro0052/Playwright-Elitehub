from playwright.sync_api import Page
from typing import Optional


class LoginPage:

    
    def __init__(self, page: Page):
     

        self.page = page
        self.url = "http://localhost:3000/"
        
        
        self.login_link = "a:has-text('Iniciar sesión')"  
        self.email_input = "#email"  
        self.password_input = "#password" 
        self.submit_button = "button[type='submit']"  
    
    
    def navigate(self) -> None:
        self.page.goto(self.url)
    
    def click_login_link(self) -> None:
        self.page.click(self.login_link)
    
    def fill_email(self, email: str) -> None:
  
        self.page.fill(self.email_input, email)
    
    def fill_password(self, password: str) -> None:
       
        self.page.fill(self.password_input, password)
    
    def click_submit(self) -> None:
        self.page.click(self.submit_button)
    
    def login(self, email: str, password: str) -> None:
      
        self.navigate()
        self.click_login_link()
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()
    
    def is_logged_in(self) -> bool:
 
        try:
            self.page.wait_for_selector(self.email_input, state="hidden", timeout=5000)
            return True
        except:
            return False
