from dotenv import load_dotenv
import os

from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import DesiredCapabilities

load_dotenv()

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--allow-running-insecure-content")  # Allow insecure content

capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

EXECUTABLE_PATH=os.environ.get("EXECUTABLE_PATH")
service = Service(executable_path=EXECUTABLE_PATH)
driver = webdriver.Chrome(options=chrome_options, service=service, desired_capabilities=capabilities) # with headless / capabilities


if __name__ == "__main__":
    # Get page source
    url = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
    driver.get(url)

    # Get page logs
    sleep(10)
    logs = driver.get_log("performance")
    for entry in logs:
        print(entry) # search for "Authorization": Bearer shr_****


    # Close the webdriver
    driver.quit()