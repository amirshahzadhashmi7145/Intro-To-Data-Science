import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get("https://www.imdb.com/chart/top/", headers = headers)
soup = BeautifulSoup(response.content, 'html5lib')
data = soup.find('ul', attrs = {'class':'ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base'})


with open('imdb_top_movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Rank', 'Title', 'Year', 'Rating', 'Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()
        for list in data.findAll('div', attrs = {'class':'sc-b0691f29-0 jbYPfh cli-children'}):
           titleWithIndex = list.div.a.h3.text.strip() #this is the title
           index, title = titleWithIndex.split('. ', 1)
           second_div = list.find_all('div')[1]
           year = second_div.find_all('span')[0].text.strip() #year
           duration = second_div.find_all('span')[1].text.strip() #duration
           rating = list.find('span', attrs = {'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'}).text.strip() #rating
           writer.writerow({'Rank': index, 'Title': title, 'Year': year, 'Rating': rating, 'Duration': duration})