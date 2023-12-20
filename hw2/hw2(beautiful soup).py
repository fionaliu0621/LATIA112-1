import requests
from bs4 import BeautifulSoup
import csv
import chardet
import os

url = 'https://www.dbas.taichung.gov.tw/16616/17599/17731/1812010/17767?PageSize=30&type=04'
response = requests.get(url)
html_content = response.content

# 使用 chardet 模組進行編碼檢測
encoding = chardet.detect(html_content)['encoding']

soup = BeautifulSoup(html_content, 'html.parser', from_encoding=encoding)

# 提取數據
data_list = []
for item in soup.find_all('div', class_='list_area'):
    # 提取序號
    serial_number = item.find('span', class_='rn').text.strip()

    # 提取標題
    title = item.find('h3').text.strip()

    # 提取張貼日
    post_date = item.find('span', class_='date').text.strip()

    data = {
        '序號': serial_number,
        '標題': title,
        '張貼日': post_date
    }
    data_list.append(data)

# 將數據寫入 CSV 檔案
csv_filename = os.path.join(os.path.expanduser('~'), 'Desktop', 'taichung_gov_data.csv')
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['序號', '標題', '張貼日']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print(f'數據已成功儲存為 {csv_filename}')