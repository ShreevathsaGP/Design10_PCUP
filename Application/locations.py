from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome
from selenium.webdriver.firefox.options import Options as Options_Firefox


class Scrape:
    def __init__(self, search):
        self.search_query = search
        self.URL = "https://www.google.com/maps/search/waste+management+organisations+"+str(self.search_query)+"/@17.5248958,78.1402979,9z"

    def scrape(self,):
        global names
        global addresses
        global websites

        names = []
        addresses = []
        websites = []

        try:
            options = Options_Chrome()
            options.headless = True
            browser = webdriver.Chrome(options=options)
            browser.get(self.URL)
        except:
            try:
                options = Options_Firefox()
                options.headless = True
                browser = webdriver.Firefox(options=options)
                browser.get(self.URL)
            except:
                print("The user does not have a compatible browser to get the data required")

        sleep(5)

        html = browser.page_source
        browser.close()

        soup = BeautifulSoup(html, 'html.parser')

        name_container = soup.find_all("h3", {"class":"section-result-title"})

        for element in name_container:
            name = element.text
            names.append(name)

        address_container = soup.find_all("span", {"jsan":"7.section-result-location"})
        for element in address_container:
            address = element.text
            if str(address) == '':
                addresses.append("Address not available")
            else:
                addresses.append(address)

        main_container = soup.findAll("div", {"class": "section-result-content"})
        for container in main_container:
            website_tag = container.find("a", {"class":"section-result-action"})
            if str(website_tag) == 'None':
                websites.append("Website not listed")
            else:
                website = website_tag['href']
                websites.append(website)

        return names, addresses, websites