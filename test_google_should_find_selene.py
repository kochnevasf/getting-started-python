
from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_size():
    browser.config.window_height = 1280
    browser.config.window_width = 1024
    browser.open('https://google.com')

    yield

    browser.close()

def test_find1(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('c'))
def test_find2(browser_size):
    browser.element('[name="q"]').should(be.blank).type('н52ккт0018ьллвдеткирврыы').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))

