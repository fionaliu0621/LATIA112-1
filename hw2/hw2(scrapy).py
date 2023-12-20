import scrapy
import csv

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://www.dbas.taichung.gov.tw/16616/17599/17731/1812010/17767?PageSize=30&type=04']

    def parse(self, response):
        data_list = []
        for item in response.css('.list_area'):
            serial_number = item.css('.rn::text').get().strip()
            title = item.css('h3::text').get().strip()
            post_date = item.css('.date::text').get().strip()

            data = {
                '序號': serial_number,
                '標題': title,
                '張貼日': post_date
            }
            data_list.append(data)

        # 將數據寫入 CSV 檔案
        csv_filename = 'output_scrapy.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['序號', '標題', '張貼日']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)

        self.log(f'數據已成功儲存為 {csv_filename}')

# To run the spider, you can use the command:
# scrapy runspider my_spider.py -o output_scrapy.json
