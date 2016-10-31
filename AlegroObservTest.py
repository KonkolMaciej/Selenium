import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class ObservationAllegroOffert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com/")
        self.driver.maximize_window()

    def test_subscribe_item(self):
        word = 'kręgiel'

        search_second_word = 'biały'
        searchFieldID = 'lst-ib'
        GoogleSearchXpath = ".//input[@type='submit' and @name = 'btnK']"
        FirstLinkXpath = ".//*[@id='rso']/div[3]/div[1]/div/div/div/span"
        wait = WebDriverWait(self.driver, 10)
        searchFieldElement = wait.until(lambda driver: driver.find_element_by_id(searchFieldID))
        GoogleSearchButton = wait.until(lambda driver: driver.find_element_by_xpath(GoogleSearchXpath))

        searchFieldElement.clear
        searchFieldElement.send_keys(word)
        GoogleSearchButton.submit()

        FirstLinkElement = wait.until(lambda driver: driver.find_element_by_xpath(FirstLinkXpath))
        Wyraz = FirstLinkElement.text.split()
        searchFieldElement.clear()
        searchFieldElement.send_keys(search_second_word)
        GoogleSearchButton.submit()

        SecondLinkXpath = ".//*[@id='rso']/div[2]/div[5]/div/div/div/span"
        SecondLinkElement = wait.until(lambda driver: driver.find_element_by_xpath(SecondLinkXpath))
        Wyraz2 = SecondLinkElement.text.split()

        self.driver.get("https://allegro.pl/")
        SearchAllegroFieldId = 'main-search-text'
        SearchAllegroButXpath = ".//input[@class='sprite search-btn']"
        SearchAllegroElement = wait.until(lambda driver: driver.find_element_by_id(SearchAllegroFieldId))
        SearchAllegroButXpath = wait.until(lambda driver: driver.find_element_by_xpath(SearchAllegroButXpath))


        SearchAllegroElement.clear()
        SearchAllegroElement.send_keys(Wyraz[2] + ' ' + Wyraz2[8])
        SearchAllegroButXpath.submit()
        sleep(5)

        OffertClickXpath = ".//*[@id='listing-offers']/section[2]/article[4]"
        OffertClickButton = wait.until(lambda driver: driver.find_element_by_xpath(OffertClickXpath))
        OffertClickButton.click()
        sleep(3)

        WatchOfferFieldId = 'watch-offer'
        WatchOfferElement = wait.until(lambda driver: driver.find_element_by_id(WatchOfferFieldId))
        WatchOfferElement.click()
        sleep(5)

    def tearDown(self):
        self.driver.close()
