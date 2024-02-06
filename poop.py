from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import csv


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
name_list = []

with open('college.csv', 'w') as result: 
    writer = csv.writer(result)
    with open('merch.csv', 'r') as file: #change the file name to the file read, and make sure that .csv is formatting
        
        
        reader = csv.reader(file)
        next(reader)
        for row in tqdm(reader):
            row_write = []
            stud_uni = row[1] #change depending on the uni placement
            row_write.append(stud_uni)

            #this block does the searching
            driver.get("https://directory.columbia.edu/people/search")
            title = driver.title
            driver.implicitly_wait(0.5)
            text_box = driver.find_element(by=By.NAME, value="filter.searchTerm")
            text_box.clear()  # Clear the search bar
            text_box.send_keys(stud_uni)
            submit_button = driver.find_element(by=By.CLASS_NAME, value="button2")
            submit_button.click()
            elements = driver.find_elements(by=By.CLASS_NAME, value="back1")
            element = elements[1]
            text = element.text
            text_after_student = text.split("Student, ", 1)[1]
            text_after_student = text_after_student.split("\n", 1)[0]

            row_write.append(text_after_student)
            name_list.append(row_write)
            

            writer.writerow(row_write)

driver.quit()

    




