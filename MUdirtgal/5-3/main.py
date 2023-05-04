import requests
from bs4 import BeautifulSoup

a = []
for i in range(0, 300, 25):
    url = 'https://www.spoj.com/RGB7/ranks2/?start='+str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='table table-condensed')


    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            rank = columns[0].text.strip()
            username = columns[1].text.strip()
            solved = columns[2].text.strip()
            # print(rank, username, solved)
            a.append([rank, username, solved])

print(a)

with open('your_file.txt', 'w') as f:
    for line in a:
        f.write(f"{line}\n")
