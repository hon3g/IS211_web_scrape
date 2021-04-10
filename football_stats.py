from bs4 import BeautifulSoup
import requests


url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

data = soup.find('tbody').text.split()
data = [data[i:i + 20] for i in range(0, len(data), 20)]

for i in data[:20]:
    print(f'Player name: {i[4]} {i[5]}')
    print(f'Position: {i[6]}')
    print(f'Team: {i[7]}')
    print(f'Touchdown passes: {i[-5]}', end='\n\n')
