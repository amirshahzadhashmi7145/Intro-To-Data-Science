import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get("https://space-facts.com/mars")
soup = BeautifulSoup(response.content, 'html5lib')
data = soup.find('table', attrs = {'id':'tablepress-p-mars-no-2'}).tbody
# print (data)

for index, _ in enumerate(range(8), start=0):
  rows = data.find_all('tr')[index]
  # print (rows)
  key = rows.find_all('td')[0].text
  value = rows.find_all('td')[1].text
  df[key] = pd.Series(value)

excel_filename = 'mars_profile_data.xlsx'
with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Mars Profile Data')