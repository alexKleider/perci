#!/usr/bin/env python3

# File: testscript.py

"""
The selenium.webdriver module provides all the
WebDriver implementations: Those currently
supported are Firefox, Chrome, IE and Remote.
The Keys class provide keys in the keyboard like
RETURN, F1, ALT etc.
The By class is used to locate elements within a
document.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("sample test case started")

driver = webdriver.Firefox()  # instance of Firefox WebDriver
# driver.maximize_window()
driver.get('https://www.python.org')  # driver.get method navigates ..
# waits until page is fully loaded ("onload" event)
# If your page uses a lot of AJAX on load then WebDriver
# may not know when it has completely loaded:
assert "Python" in driver.title
# WebDriver offers a number of ways to find elements
# using the find_element method. For example, the
# input text element can be located by its name
# attribute using the find_element method and using
# By.NAME as its first parameter. A detailed
# explanation of finding elements is available in
# the Locating Elements chapter. 
# https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
elem = driver.find_element(By.NAME, 'q')
# Next, we are sending keys, this is similar to
# entering keys using your keyboard. Special keys
# can be sent using Keys class imported from
# selenium.webdriver.common.keys. To be safe, we’ll
# first clear any pre-populated text in the input
# field (e.g. “Search”) so it doesn’t affect our
# search results:
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# After submission of the page, you should get the
# result if there is any. To ensure that some results
# are found, make an assertion:
assert "No results found." not in driver.page_source
# Finally, the browser window is closed. You can
# also call quit method instead of close. The quit
# will exit entire browser whereas close will close
# one tab, but if just one tab was open, by default
# most browser will exit entirely.:
driver.close()
print("sample test case successfully completed")

