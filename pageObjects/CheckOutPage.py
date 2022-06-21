from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage():

    def __init__(self, driver):
        self.driver = driver


    products = (By.XPATH, "//div[@class='card h-100']")
    CheckoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    Checkout_end = (By.XPATH, "//button[@class='btn btn-success']")
    Checkout_text = (By.XPATH, "//tr/td[1]/div/div/h4/a")
    def getProductsList(self, product_name):

        for product in self.driver.find_elements(*CheckOutPage.products):
            if product.find_element(By.XPATH, "div/h4/a").text == product_name:
                final_product = product.find_element(By.XPATH, "div/button")

        return final_product

    def getCheckoutButton(self):

        return self.driver.find_element(*CheckOutPage.CheckoutButton)

    def getVerifyingText(self):

        return self.driver.find_element(*CheckOutPage.Checkout_text)

    def getCheckOutEnd(self):
        self.driver.find_element(*CheckOutPage.Checkout_end).click()
        confirmpage = ConfirmPage(self.driver)  # we create an instance of CorfirmPage
        return confirmpage

