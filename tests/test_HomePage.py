import time

import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_Form(self, getData):
        log = self.getLogger() #This will be logged in a file in the project(tets/utilities/report.html)
        time.sleep(1)
        locator = [0, 0, 1]
        list_names = ["name", "email", "exampleInputPassword1"]
        values = [getData["Name"], getData["Email"], getData["Password"]]
        # fill out name and email and fill out password
        homePage = HomePage(self.driver)

        homePage.textBox_list(list_names, values, locator)

        homePage.click(By.ID, "exampleCheck1")

        time.sleep(1)

        homePage.click(By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']")
        time.sleep(1)

        homePage.dropdown(By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']","Female","class")

        time.sleep(1)

        homePage.dropdown(By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']",0,"index")

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='date']")
        time.sleep(1)

        homePage.click(By.XPATH, "//input[@type='submit']")
        time.sleep(1)

        message = homePage.getText(By.XPATH, "//div[contains(@class,'alert alert-success')]")
        log.info(message)

        log.info(homePage.getTitle())

        assert "Success!" in message

        print(self.driver.current_url)

        self.driver.refresh()
        #self.driver.minimize_window()

        #self.driver.back()

        #time.sleep(5)


    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param