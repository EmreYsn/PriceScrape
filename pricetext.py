import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MyPriceCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_price(self):
        self.driver.maximize_window()

        self.driver.get("https://www.mediamarkt.com.tr/?utm_content=brand&gad_source=1&gclid=Cj0KCQjwtsy1BhD7ARIsAHOi4xbA8FgmzqZVv7EJWHQevl_ZpfC6tdsA4Qm04GTKfDy6bCrbbJXt2PYaAhp3EALw_wcB&gclsrc=aw.ds")
        search_stick = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/header/div/div/div[3]/div/div/form/div/div/input")
        search_stick.click()
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/header/div/div/div[3]/div/div/form/div/div/input")))
        search_stick.send_keys("telefon")
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/header/div/div/div[3]/div/div/form/div/div/div[1]/button")
        search_button.click()
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/main/div[1]/div/div/div/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/span[1]")))
        test_price = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div[1]/div/div/div/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/span[1]")
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/main/div[1]/div/div/div/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/span[1]")))
        print(f"Price: {test_price.text}")


if __name__ == '__main__':
    unittest.main()
