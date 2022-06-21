import time

from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage

from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # we use asterix because we are dealing with a tuple
        checkout = CheckOutPage(self.driver) # we create an instance of CheckOutPage
        return checkout

    def textBox_list(self, list_names, values, locator):

        for i, n, m in zip(list_names, values, locator):
            if (m == 0):
                self.driver.find_element(By.NAME, i).send_keys(n)
            else:
                self.driver.find_element(By.ID, i).send_keys(n)
            time.sleep(1)

    def click(self, by, locator_text):

        self.driver.find_element(by, locator_text).click()

    def dropdown(self, by, locator_text, option, type):
        dropdown = self.select(by, locator_text)
        if type=="class":
            time.sleep(1)
            dropdown.select_by_visible_text(option)
        elif type=="index":
            time.sleep(1)
            dropdown.select_by_index(option)

    def getText(self, by, locator_text):
        return self.driver.find_element(by, locator_text).text

    def getTitle(self):

        return self.driver.title