""" Plays the typeracer game by itself. """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

import time


class TypeRacerBot(object):
    def __init__(self):
        self.logged_in = False
        self.driver = webdriver.Chrome()
        self.driver.get("https://play.typeracer.com/")
        self.is_loaded = False

    def enter_race(self):
        try:
            self.driver.find_element_by_css_selector('.mainMenu  a.gwt-Anchor').click()
        except NoSuchElementException:
            print('Content not loaded yet. Trying again in 1 sec')
            time.sleep(1)
            self.enter_race()
        else:
            pass

    def start_test(self):
        # Begin test
        self.driver.find_element_by_css_selector('.gwt-Button').click()

        # Take sentence input from user
        test_input = input("Start typing now:\n")

        text_area = self.driver.find_element_by_css_selector('.challengeTextArea')
        text_area.send_keys(test_input)
        self.driver.find_element_by_css_selector('button.gwt-Button').click()

    def login(self):
        try:
            self.driver.find_element_by_css_selector('.gwt-Anchor').click()
            self.driver.find_element_by_css_selector('input.gwt-TextBox').send_keys('chuck616')
            self.driver.find_element_by_css_selector('input.gwt-PasswordTextBox').send_keys('tr123456')
            self.driver.find_element_by_css_selector('button.gwt-Button').click()
        except NoSuchElementException:
            print('No element found')
        else:
            print('Logged in successfully')
            self.logged_in = True

    def run(self):
        time.sleep(3)
        # self.login()
        self.enter_race()
        time.sleep(2)
        txtbox = self.driver.find_element_by_css_selector('input.txtInput')

        while txtbox.get_attribute('disabled'):
            time.sleep(0.7)
            print('still disabled')

        # time.sleep(15)
        # txtbox = driver.find_element_by_css_selector('input.txtInput')

        css = "#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div"
        # css = "#gwt-uid-16 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div"
        # css = "#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div"

        words = self.driver.find_element_by_css_selector(css)

        word_list = words.text.split(" ")

        for word in word_list:
            txtbox.send_keys(word)
            txtbox.send_keys(Keys.SPACE)
            time.sleep(0.20)

        # self.start_test()


if __name__ == '__main__':
    bot = TypeRacerBot()
    bot.run()

