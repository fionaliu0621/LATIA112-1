from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import csv

# 設定 Chrome 驅動程式的路徑
driver_path = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"


# 創建 ChromeService
chrome_service = ChromeService(executable_path=driver_path)

# 使用 ChromeService 創建 WebDriver
driver = webdriver.Chrome(service=chrome_service)

# ... 其餘程式碼 ...



# 前往指定網頁
url = "https://www.dbas.taichung.gov.tw/16616/17599/17731/1812010/17767?PageSize=30&type=04"
driver.get(url)

# 使用 Selenium 等待直到頁面完全加載
driver.implicitly_wait(10)

# 提取數據
data_list = []
for item in driver.find_elements(By.CLASS_NAME, 'list_area'):
    serial_number = item.find_element(By.CLASS_NAME, 'rn').text.strip()
    title = item.find_element(By.TAG_NAME, 'h3').text.strip()
    post_date = item.find_element(By.CLASS_NAME, 'date').text.strip()

    data = {
        '序號': serial_number,
        '標題': title,
        '張貼日': post_date
    }
    data_list.append(data)
                  
# 關閉瀏覽器
driver.quit()

# 將數據寫入 CSV 檔案
csv_filename = 'output.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['序號', '標題', '張貼日']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print(f'數據已成功儲存為 {csv_filename}')
