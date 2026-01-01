from cmath import exp

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import  LoginPage
from pages.my_account_page import MyAccountPage
from config import Config

@pytest.mark.regression
def test_user_logout(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = MyAccountPage(page)


    home_page.click_my_account()
    home_page.click_login()

    login_page.set_email(Config.email)
    login_page.set_password(Config.password)
    login_page.click_login()

    expect(account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)

    logout_page = account_page.click_logout()

    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)

    logout_page.click_continue()

    expect(page).to_have_title("Your Store")