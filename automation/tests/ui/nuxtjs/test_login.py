import pytest
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parents[4] / "pages"))

from nuxtjs.login_page import LoginPage


class TestLoginNuxt:
    
    
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        
        login_page.login(
            email="mariaeugenialopez456@gmail.com",
            password="1234"
        )
        
   
        assert login_page.is_logged_in(), "Login was not successful"
    
    def test_login_step_by_step(self, page):
        login_page = LoginPage(page)
        
      
        login_page.navigate()
        
       
        login_page.click_login_link()
        
    
        login_page.fill_email("mariaeugenialopez456@gmail.com")
        
       
        login_page.fill_password("1234")
        
        
        login_page.click_submit()
        
     
        assert login_page.is_logged_in(), "Login was not successful"
