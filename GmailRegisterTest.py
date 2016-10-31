import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class TestGmailRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://gmail.com/")

    def test_Register(self):

        Name = 'YourName'
        Surname = 'YourSurname'
        PasswordGmail = 'YourPassword@'
        PasswordConfirm = 'YourPassword@'
        BirthYear = '1994'
        GmailName = 'HereYourNewEmailAdress'
        MonthBirth = 'Pazdziernik'
        DayBirth = '25'
        Gender = 'Mezczyzna'

        registerButtonXpath = "//a[contains(@href, 'SignUp?service')]"
        optionMonthButtonXpath = ".//*[@id='BirthMonth']/div[1]"
        GenderButtonXpath = ".//*[@id='Gender']/div[1]"
        FirstNameFieldId = 'FirstName'
        LastNameFieldId = 'LastName'
        GmailAddressFieldId = 'GmailAddress'
        PasswordFieldId = 'Passwd'
        ConfirmPasswordFieldId = 'PasswdAgain'
        BirthYearFieldId = 'BirthYear'
        BirthDayFieldId = 'BirthDay'

        registerButtonElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(registerButtonXpath))
        registerButtonElement.click()

        wait = WebDriverWait(self.driver, 10)

        FirstNameElement = wait.until(lambda driver: driver.find_element_by_id(FirstNameFieldId))
        LastNameElement = wait.until(lambda driver: driver.find_element_by_id(LastNameFieldId))
        GmailAddressElement = wait.until(lambda driver: driver.find_element_by_id(GmailAddressFieldId))
        PasswordElement = wait.until((lambda driver: driver.find_element_by_id(PasswordFieldId)))
        ConfirmPasswordElement = wait.until((lambda driver: driver.find_element_by_id(ConfirmPasswordFieldId)))
        BirthYearElement = wait.until(lambda  driver: driver.find_element_by_id(BirthYearFieldId))
        optionMonthButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(optionMonthButtonXpath))
        BirthDayElement = wait.until(lambda driver: driver.find_element_by_id(BirthDayFieldId))
        GenderButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(GenderButtonXpath))

        FirstNameElement.clear()
        FirstNameElement.send_keys(Name)
        LastNameElement.clear()
        LastNameElement.send_keys(Surname)
        GmailAddressElement.clear
        GmailAddressElement.send_keys(GmailName)
        PasswordElement.clear
        PasswordElement.send_keys(PasswordGmail)
        ConfirmPasswordElement.clear
        ConfirmPasswordElement.send_keys(PasswordConfirm)
        BirthYearElement.clear
        BirthYearElement.send_keys(BirthYear)
        optionMonthButtonElement.click
        optionMonthButtonElement.send_keys(MonthBirth)
        BirthDayElement.clear
        BirthDayElement.send_keys(DayBirth)
        GenderButtonElement.click
        GenderButtonElement.send_keys(Gender)

        CheckBox = "SkipCaptcha"
        self.driver.find_element_by_id(CheckBox).click()

        #next step
        NextStepButtonXpath = ".//*[@id='submitbutton']"
        NextStepButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(NextStepButtonXpath))
        NextStepButtonElement.submit()
        time.sleep(4)

        #scrolowanie
        ElementDown= ".//*[@id='tos-text']/div[5]"
        ScroolDownElement = wait.until(lambda driver: driver.find_element_by_xpath(ElementDown))
        ScroolDownElement.location_once_scrolled_into_view
        time.sleep(4)

        AgreeButton = "iagreebutton"
        AgreeButtonElement = wait.until(lambda driver: driver.find_element_by_id(AgreeButton))
        AgreeButtonElement.click()

        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

