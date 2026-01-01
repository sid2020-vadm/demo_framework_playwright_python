import time

import pytest
from playwright.sync_api import expect

from config import Config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.mark.sanity
@pytest.mark.regression
def test_product_search(page):
    product_name = Config.product_name
    search_results_page = SearchResultsPage(page)
    home_page = HomePage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()

    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)
    expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)
