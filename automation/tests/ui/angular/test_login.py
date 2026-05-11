import pytest
import sys
from pathlib import Path

# Agregar la carpeta de páginas al path para importar
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "pages"))

from angular.login_page import LoginPage


class TestLoginAngular:
    """Tests for login functionality in Angular."""
    
    def test_successful_login(self, page):
        """
        Test that verifies a successful login.
        - Navigate to the URL
        - Click on "Iniciar sesión"
        - Fill email: mariaeugenialopez456@gmail.com
        - Fill password: 1234
        - Click on the submit button
        """
        # Instantiate the Page Object Model
        login_page = LoginPage(page)
        
        # Execute the login flow
        login_page.login(
            email="mariaeugenialopez456@gmail.com",
            password="1234"
        )
        
        # Verify that login was successful
        assert login_page.is_logged_in(), "Login was not successful"
    
    def test_login_step_by_step(self, page):
        """
        Test that verifies login step by step (without using the combined login method).
        Useful for debugging.
        """
        login_page = LoginPage(page)
        
        # Step 1: Navigate to the URL
        login_page.navigate()
        
        # Step 2: Click on "Iniciar sesión"
        login_page.click_login_link()
        
        # Step 3: Fill email
        login_page.fill_email("jabravoe@siesa.com")
        
        # Step 4: Fill password
        login_page.fill_password("1234")
        
        # Step 5: Click on the login button
        login_page.click_submit()
        
        # Verification
        assert login_page.is_logged_in(), "Login was not successful"
