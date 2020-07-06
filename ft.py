#!/usr/bin/env python3

# File: ft.py (functional_tests.py)

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to check home page of cool app:
        self.browser.get('http://localhost:8000')

        # She notices title and header mention to-do lists:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She types "Buy peacock feathers" into a text box:

        # Upon hitting enter, the page updates showing a list:
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box for adding another item.
        # She enters "Use peacock feathers to make a fly"

        # Page again updates showing both items on her list.

        # Will site remember her list? Then she sees a unique URL has
        # been generated for her with explanatory text to that effect.

        # She visits that url and sees her list.

        # Satisfied

if __name__ == '__main__':
    unittest.main(warnings='ignore')
