from selenium import webdriver
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import time

def scrape(title_key, location_key):

    output = []
    count = 1
    titles, companies, locations, links = [], [], [], []


    browser = webdriver.Firefox(executable_path='geckodriver.exe')
    browser.get('https://uk.linkedin.com/jobs')

    title = browser.find_element_by_name('keywords')
    title.send_keys(title_key)

    browser.find_element_by_name('location').clear()
    location = browser.find_element_by_name('location')
    location.send_keys(location_key)

    title.submit()
    time.sleep(2)

    browser.find_element_by_xpath("//ul[@class='filters__list']/li[1]/div[1]/div[1]/button[1]").click()
    browser.find_element_by_xpath("//label[@for='sortBy-1'][1]").click()
    browser.find_element_by_xpath("//button[@class='filter__submit-button']").click()

    time.sleep(1)

    url = browser.current_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("ul", class_="jobs-search__results-list")

    jobs = results.find_all("div", class_="base-search-card__info")
    
    elems = browser.find_elements_by_xpath("//a[starts-with(@class, 'base-card')]")
    for elem in elems:
        links.append(elem.get_attribute("href"))

    for job in jobs:
    
        titles.append(job.find("h3", class_="base-search-card__title").text.strip())
        companies.append(job.find("h4", class_="base-search-card__subtitle").text.strip())
        locations.append(job.find("span", class_="job-search-card__location").text.strip())

        count += 1
    
    browser.close()
    output = [titles, companies, locations, links]

    return output
