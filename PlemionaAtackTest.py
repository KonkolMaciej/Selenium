import time

# from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class TestPlemionaAttack(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/maciek/projekty/selenium/chromedriver')
            # driver = webdriver.Firefox()
        self.driver.get("https://plemiona.pl/")
        self.driver.maximize_window()

    def test_Login_and_Attack(self):
        # define variables
        wait = WebDriverWait(self.driver, 10)
        login = 'login'
        password = 'password'
        loginFieldpmXpath = ".//*[@id='user']"
        passwordButtonXpath = ".//*[@id='password']"
        rememberMeCheckXpath = ".//*[@id='cookie']"
        loginButtonXpath = ".//*[@id='js_login_button']/a/span[2]"
        checkSerwerButtonXpath = ".//*[@id='active_server']/div[1]/a[2]/span"

        # search element
        loginFieldElement = wait.until(lambda driver: driver.find_element_by_xpath(loginFieldpmXpath))
        passwordButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(passwordButtonXpath))
        rememberMeCheckElement = wait.until(lambda driver: driver.find_element_by_xpath(rememberMeCheckXpath))
        loginButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        # Insert login and password
        loginFieldElement.clear
        loginFieldElement.send_keys(login)
        passwordButtonElement.clear
        passwordButtonElement.send_keys(password)
        rememberMeCheckElement.click()
        loginButtonElement.click()
        # Check world
        CheckSerwerButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(checkSerwerButtonXpath))

        CheckSerwerButtonElement.click()
        time.sleep(4)


        wait = WebDriverWait(self.driver,10)
        placeButtonXpath = ".//*[@id='show_summary']/div/div/div[21]/a"
        placeTargetFieldXpath = ".//*[@id='place_target']/input"
        cordAttack = "573|573"

        placeButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(placeButtonXpath))

        placeButtonElement.click()

        placeTargetFieldElement = wait.until(lambda driver: driver.find_element_by_xpath(placeTargetFieldXpath))
        placeTargetFieldElement.send_keys(cordAttack)

        #choose all unit
        allUnitXpath = ".//*[@id='selectAllUnits']"
        allUnitElement = wait.until(lambda driver: driver.find_element_by_xpath(allUnitXpath))
        allUnitElement.click()

        #attack button
        attackButtonXpath = ".//*[@id='target_attack']"
        attackButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(attackButtonXpath))
        attackButtonElement.click()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

