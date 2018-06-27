# -*- coding: utf-8 -*-

"""Page object model for login."""

from pypom import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected


class LoginPage(Page):
    """Page object model for the login."""

    URL_TEMPLATE = "/{org}/login/"

    _alert_locator = (By.CSS_SELECTOR, ".alert-danger")
    _input_email_locator = (By.ID, "inputEmail")
    _input_password_locator = (By.ID, "inputPassword")
    _login_buttton_locator = (By.CSS_SELECTOR, "button[type='submit']")

    @property
    def title(self):
        """Return the page title."""
        return self.wait.until(lambda s: self.selenium.title)

    @property
    def alert(self):
        """Return the alert element."""
        element = self.wait.until(
            expected.visibility_of_element_located(self._alert_locator)
        )
        return element.text

    def enter_email(self, email):
        """Enter the given user email."""
        input_email = self.find_element(*self._input_email_locator)
        input_email.send_keys(email)

    def enter_password(self, password):
        """Enter the given user password."""
        input_password = self.find_element(*self._input_password_locator)
        input_password.send_keys(password)

    def click_login(self):
        """Click the login button."""
        btn = self.find_element(*self._login_buttton_locator)
        btn.click()

    def login(self, email="", password=""):
        """Log in the user with the given credentials."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        from pages.home import HomePage

        return HomePage(self.selenium).wait_for_page_to_load()
