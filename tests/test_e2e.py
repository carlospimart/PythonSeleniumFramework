
import time

#@pytest.mark.usefixtures("setup") # we don't need that anymore as we already inherit this from
# BaseClass
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        # we create an instance of HomePage
        log = self.getLogger()
        homepage = HomePage(self.driver)

        time.sleep(1)

        checkout = homepage.shopItems() # We call one element from homepage, and we click it


        time.sleep(1)

        checkout.getProductsList("Blackberry").click()

        time.sleep(1)

        checkout.getCheckoutButton().click()

        time.sleep(1)

        ProductName = checkout.getVerifyingText().text

        assert ProductName == "Blackberry"
        log.info(ProductName)
        print(ProductName)
        time.sleep(1)

        confirmpage = checkout.getCheckOutEnd()

        time.sleep(1)

        log.info("Entering country name as Ind")
        confirmpage.getCountryList("India").click()



        confirmpage.getCheckBox().click()

        time.sleep(1)

        confirmpage.getPurchaseButton().click()

        time.sleep(2)

        message = confirmpage.getMessageSuccess().text
        log.info("Text received from application is: "+message)
        assert "Success! Tlhank you!" in message

        self.driver.get_screenshot_as_file("Screenshot.png")
