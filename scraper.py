import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    jobs = []
    for tr in soup.find_all('tr', class_='job'):
        title = tr.find('h2')
        company = tr.find('h3')
        link = tr.get('data-href')

        if title and company and link:
            jobs.append({
                'title': title.get_text(strip=True),
                'company': company.get_text(strip=True),
                'link': "https://remoteok.com" + link
            })
    return jobs
