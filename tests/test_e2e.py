import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.my_account_page import MyAccountPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from config import Config
from utils.random_data_util import RandomDataUtil

@pytest.mark.end_to_end
def test_e2e(page):
    email,password =perform_registration(page)

    perform_logout(page)

    perform_login(page, email, password)

    add_product_to_cart(page)

    verify_shopping_cart(page)



def perform_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data_utl = RandomDataUtil()

    email = random_data_utl.get_email()
    password = random_data_utl.get_password()


    registration_page.set_first_name(random_data_utl.get_first_name())
    registration_page.set_last_name(random_data_utl.get_last_name())
    registration_page.set_email(email)
    registration_page.set_telephone(random_data_utl.get_phone_number())
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)
    registration_page.set_privacy_policy()
    registration_page.click_continue()
    confirmation_message = registration_page.get_confirmation_msg()
    expect(confirmation_message).to_have_text("Your Account Has Been Created!")

    return email,password

def perform_logout(page):
    account_page = MyAccountPage(page)
    logout_page = LogoutPage(page)

    account_page.click_logout()
    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)
    logout_page.click_continue()
    expect(page).to_have_title("Your Store")

def perform_login(page,email,password):
    homepage = HomePage(page)
    loginpage = LoginPage(page)
    accountpage = MyAccountPage(page)
    homepage.click_my_account()
    homepage.click_login()
    loginpage.set_email(email)
    loginpage.set_password(password)
    loginpage.click_login()
    expect(accountpage.get_my_account_page_heading()).to_be_visible(timeout=3000)

def add_product_to_cart(page):
    product_name = Config.product_name
    quantity = Config.product_quantity

    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()
    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)
    expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)

    product_page = search_results_page.select_product(product_name)
    product_page.set_quantity(quantity)
    product_page.add_to_cart()
    expect(product_page.get_confirmation_message()).to_be_visible(timeout=3000)

def verify_shopping_cart(page):
    product_page = ProductPage(page)
    product_page.click_items_to_navigate_to_cart()

    shopping_cart = product_page.click_view_cart()
    print("Navigated to shopping cart page")
    expect(shopping_cart.get_total_price()).to_have_text(Config.total_price)



