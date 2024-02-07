from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

read_rows = []
date = '2024-02-07' #change the date to the format as follows YYYY-MM-DD
seats_number = '2' #change to number 2-6


with open('resy-confirm.csv', 'r') as fread:
    reader = csv.reader(fread)
    next(reader)
    for row in tqdm(reader):
        print(row)
        read_rows.append(row)

with open('resy-confirm.csv', 'w') as fwrite:
    writer = csv.writer(fwrite)
    writer.writerow(['Link', 'Restaurant Name', 'Yes/No'])

    for row in read_rows:
        link = row[0] + '?date=' + date + '&seats=' + seats_number
        print(link)
        driver.get(link)
        title = driver.title      
        try:
            elements = WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located((
                    By.CLASS_NAME, "ShiftInventory__availability-message"
                ))
            )  
            row[2] = 'No' 
        except:
            row[2] = 'Yes'
            
        writer.writerow(row)
        
driver.quit()
    
