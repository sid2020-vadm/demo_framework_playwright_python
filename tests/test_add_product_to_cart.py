from re import search

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config

@pytest.mark.regression
def test_add_product_to_cart(page):
    product_name  = Config.product_name
    quantity = Config.product_quantity

    home_page = HomePage(page)
    search_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()

    product_page = search_page.select_product(product_name)

    product_page.set_quantity(quantity)
    product_page.add_to_cart()

    expect(product_page.get_confirmation_message()).to_be_visible(timeout=3000)
