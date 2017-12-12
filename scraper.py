"""Stackoverflow job scraper."""
from bs4 import BeautifulSoup as BS

import requests


def stack_parser():
    """Parse stackoverflow for python jobs and return CSV."""
    for i in range(1, 10):
        url = f'https://stackoverflow.com/jobs?pg={i}'
        r = requests.get(url)
        soup = BS(r.content, 'html.parser')
        page_res = soup.find_all('div', class_='-job')
        py_tag = soup.find_all(string='python', class_='post-tag') 
        parent = py_tag.find_parent(class_='-job-summary')
        title = parent.find('a').text
        company = parent.find(class_='-name').text.strip()
        location = parent.find(class_='-location').contents[0].strip()
        date_posted = parent.find(class_='-posted-date').text.strip()
        link = parent