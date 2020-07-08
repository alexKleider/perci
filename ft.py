#!/usr/bin/env python3

# File: ft.py (functional_tests.py)

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

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

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter an item into the to do list:
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.getitem('place_holder'),
                        'Enter a to-do item')


        # She enters 'Buy peacock feathers':
        inputbox.send_keys("Buy peacock feathers")

        # Upon hitting enter, the page updates showing a list:
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers'
                            for row in rows))

        # There is still a text box inviting her to enter another item
        # She enters 'Use peacock feathers to make a fly'

        self.fail('Finish the test!')



        # Page again updates showing both items on her list.

        # Will site remember her list? Then she sees a unique URL has
        # been generated for her with explanatory text to that effect.

        # She visits that url and sees her list.

        # Satisfied

if __name__ == '__main__':
    unittest.main(warnings='ignore')
