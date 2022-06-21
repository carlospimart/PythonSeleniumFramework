import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler  object

        logger.setLevel(logging.INFO)

        return logger

    def verifyLinkPressence(self, text):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def select(self,by, locator_text):
        dropdown = Select(self.driver.find_element(by, locator_text))
        return dropdown