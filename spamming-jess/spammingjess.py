import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def get_first_name():
    random_list = [
        "Connor",
        "Nguyen",
        "Geoffrey",
        "Aaron",
        "Dale",
        "Lebron",
        "Steph",
        "Klay",
        "Jeffrey",
        "Bolu",
        "Jackson",
        "Rishi",
        "Aaron"
    ]

    return random.choice(random_list)

def get_last_name():
    random_list = [
        "Li",
        "Tran",
        "Wu",
        "Yu",
        "Martin",
        "Bolar",
        "Davis",
        "Soni",
        "Epstein",
        "Koletsos",
        "Janus",
        "Skibidi",
        "Lebron"
    ]

    return random.choice(random_list)


def get_email():
    random_list = [
        "gmail",
        "yahoo",
        "hotmail",
        "outlook",
        "aol",
        "protonmail",
        "tutanota",
        "zoho",
        "icloud",
        "yandex",
        "mail",
        "gmx",
        "mailfence"
    ]

    return f"lebronthegoat{random.randint(690,4200)}@{random.choice(random_list)}.com"


# Function to generate a random sentence
def generate_random_sentence():
    subjects = ["The cat", "A scientist", "My neighbor", "The teacher", "An astronaut", "A dog"]
    verbs = ["jumps", "runs", "writes", "discovers", "teaches", "eats"]
    objects = ["a book", "the moon", "a sandwich", "the floor", "a mystery", "a computer"]
    adjectives = ["quickly", "happily", "silently", "eagerly", "gracefully", "brilliantly"]


    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    if random.choice([True, False]):  # Randomly decide whether to add an adjective
        adj = random.choice(adjectives)
        sentence = f"{subject} {verb} {obj} {adj}."
    else:
        sentence = f"{subject} {verb} {obj}."
    return sentence

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
            #submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

            fname_field.send_keys(get_first_name())
            time.sleep(random.randint(1,3)/4 * 3)
            lname_field.send_keys(get_last_name())
            time.sleep(random.randint(1,3)/4 * 3)
            email_field.send_keys(get_email())
            time.sleep(random.randint(1,3)/4 * 3)
            describe_business.send_keys(generate_random_sentence())
            time.sleep(random.randint(1,3)/4 * 3)
            describe_project.send_keys(generate_random_sentence())
            time.sleep(random.randint(1,3)/4 * 3)

            submit_button = driver.find_element(By.CLASS_NAME, "form-submit-button")
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).perform()
            submit_button.click()
            actions.move_to_element(describe_project).perform()
            time.sleep(random.randint(1,3)/4 * 3)

            driver.refresh()

            time.sleep(random.randint(1,5)/4 * 3)

    except KeyboardInterrupt:
        print("Loop interrupted by user.")

    finally:
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spam Jessica's contact form.")
    parser.add_argument('--iter', type=int, default=None, help='Number of iterations (default: 1)')
    
    args = parser.parse_args()

    spam_jess(number_of_iterations=args.iter)