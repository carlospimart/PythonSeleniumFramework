from selenium.webdriver.common.by import By
import time

from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    box = (By.ID, "country")
    countries_list = (By.XPATH, "//div[@class='suggestions']")
    elements = (By.XPATH, "ul/li/a")
    purchaseButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    def getCountryList(self, country):

        self.driver.find_element(*ConfirmPage.box).send_keys("ind")

        self.verifyLinkPressence(country)
        countries = self.driver.find_elements(*ConfirmPage.countries_list)

        time.sleep(1)

        for i in countries:

            if i.find_element(*ConfirmPage.elements).text == country:
                selected_country = i.find_element(*ConfirmPage.elements)
                break

        time.sleep(3)

        return selected_country

    def getCheckBox(self):

        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):

        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getMessageSuccess(self):

        return self.driver.find_element(*ConfirmPage.message)
