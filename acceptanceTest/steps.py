from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@before.all
def set_browser():
    world.browser = webdriver.Firefox()

@step(r'acceso a la URL "([^"]*)"')
def access_url(step, url):
    world.browser.get(url)

@step(r'veo el encabezado "([^"]*)"')
def see_header(step, text):
    header = world.browser.title
    assert header == text
