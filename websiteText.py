import requests
from bs4 import BeautifulSoup

url = 'https://hospitality.uoguelph.ca/hours-menus-feedback/daily-menus/creelman-hall-daily-menus'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

page_text = soup.get_text()

paragraph = [p.get_text() for p in soup.find_all('p')]

print(page_text)
print(paragraph)





