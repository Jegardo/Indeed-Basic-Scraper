import requests
from bs4 import BeautifulSoup

URL = 'https://de.indeed.com/Jobs?q=Softwareentwickler&l=Hamburg'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
# python_jobs = results.find_all('h2', string=lambda text: "python" in text.lower())
# print(len(python_jobs))

# for p_job in python_jobs:
#    link = p_job.find('a')['href']
#    print(p_job.text.strip())
#    print(f"Apply here: {link}\n")
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find('div', class_='location')
    ez_apply = title_elem.find('a')['href']
    if not location_elem:
        location_elem = job_elem.find('span', class_='location')
    print()
    print(title_elem.text, company_elem.text)
    print(location_elem.text)
    print
    print(f"Apply here: {ez_apply}\n")
