from bs4 import BeautifulSoup
import requests
import re


url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

match = re.search('1/3 8:20 ET.*?At LA Rams', soup.text, re.DOTALL)
data = match[0].split('\n\n\n')

for i in range(len(data)):
    data[i] = data[i].split('\n')

for i in data:
    print(f'Favorite: {i[1]}')
    print(f'Underdog: {i[3]}')
    print(f'Spread: {i[2]}', end='\n\n')
