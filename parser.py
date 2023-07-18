import urllib.request
from bs4 import BeautifulSoup

url = 'Enter a link to the site'
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if href and (href.startswith('http://') or href.startswith('https://')):
        print(href)
