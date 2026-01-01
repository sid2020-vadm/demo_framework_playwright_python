import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.random_data_util import RandomDataUtil

@pytest.mark.sanity
@pytest.mark.regression
def test_user_registration(page):
    home_page=HomePage(page)
    registration_page =RegistrationPage(page)
    random_data_utl = RandomDataUtil()
    home_page.click_my_account()
    home_page.click_register()

    email=random_data_utl.get_email()
    print(f"email is {email}")
    password = random_data_utl.get_password()
    print(f"password is {password}")

    registration_page.set_first_name(random_data_utl.get_first_name())
    registration_page.set_last_name(random_data_utl.get_last_name())
    registration_page.set_email(email)
    registration_page.set_telephone(random_data_utl.get_phone_number())
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    confirmation_message =registration_page.get_confirmation_msg()
    expect(confirmation_message).to_have_text("Your Account Has Been Created!!")
