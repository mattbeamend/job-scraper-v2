from bs4 import BeautifulSoup
import requests

def scrape(title, location):

    output = []

    titles = []
    companys = []
    locations = []
    links = []
    
    count = 0

    title = title.replace(' ', '+')
    location = location.replace(' ', '+')

    url = "https://uk.indeed.com/jobs?q=" + title + "&l=" + location + "&sort=date"
    print(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="resultsCol")
    
    jobs = results.find_all("td", class_="resultContent")

    results = soup.find(id="mosaic-provider-jobcards")
    for link in results.select('a[class*="tapItem fs-unmask result job_"]'):
        links.append("https://uk.indeed.com" + link.get("href"))

    for job in jobs:
        
        spans = job.find_all("span")
        for span in spans:
            if span.text == "new": continue
            title = span.text
            break
            
        company = job.find("span", class_="companyName").text
        location = job.find("div", class_="companyLocation").text

        titles.append(title)
        companys.append(company)
        locations.append(location)

        count += 1

    output = [titles, companys, locations, links]

    return output