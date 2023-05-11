from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://fr.indeed.com/jobs?q=data+scientist&l=&vjk=4ff9ff31cc2e42b9').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_= "cardOutline tapItem fs-unmask result job_e567956e34d8e384 sponsoredJob resultWithShelf sponTapItem desktop vjs-highlight css-kyg8or eu4oa1w0")
#print(jobs)
company_name  = jobs.find('h3', class_='').text.replace(' ', '')

for job in jobs: 
    company_name = job.find('h3', class_ = '').text.replace(' ', '')
    skills = job.find('span', class_ = '').text.replace(' ', '')
    published_date = job.find('span', class_='').span.text
    #print(published_date)
    more_info = job.header.h2.a
    print(f'More info:{more_info}')
    print(f'Company name:{company_name.strip()}')
    print(f'Skills:{skills.strip()}')





