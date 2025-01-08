import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def spam_jess(number_of_iterations=None):

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.jessicabolar.com/contact")
    count = 0

    try:
        while True:
            if number_of_iterations is not None and count == number_of_iterations:
                break

            count += 1

            wait = WebDriverWait(driver, 10)
            fname_field = wait.until(EC.presence_of_element_located((By.ID, "name-yui_3_17_2_1_1564674081737_5858-fname-field")))
            lname_field = wait.until(EC.presence_of_element_located((By.ID, "name-yui_3_17_2_1_1564674081737_5858-lname-field")))
            email_field = wait.until(EC.presence_of_element_located((By.ID, "email-yui_3_17_2_1_1564674081737_5859-field")))
            describe_business = wait.until(EC.presence_of_element_located((By.ID, "textarea-yui_3_17_2_1_1564673948220_25800-field")))  
            describe_project = wait.until(EC.presence_of_element_located((By.ID, "textarea-yui_3_17_2_1_1564673948220_26771-field")))
            submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

            fname_field.send_keys("Hugh")
            lname_field.send_keys("Janus")
            email_field.send_keys("getspammed@gmail.com")
            describe_business.send_keys("LOL I figured out how to spam ur website")
            describe_project.send_keys("Get wrekt you n00b")
            time.sleep(1)  

            submit_button.click()
            time.sleep(2)

            driver.refresh()

            time.sleep(2)

    except KeyboardInterrupt:
        print("Loop interrupted by user.")

    finally:
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spam Jessica's contact form.")
    parser.add_argument('--iter', type=int, default=None, help='Number of iterations (default: 1)')
    
    args = parser.parse_args()

    spam_jess(number_of_iterations=args.iter)