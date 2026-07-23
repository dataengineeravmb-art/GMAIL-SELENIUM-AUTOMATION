from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

print("BISMILLAH")
Chromeoption = webdriver.ChromeOptions()
def Gmail_Login(Mail_Directory,Email,Password,Send_TO,Send_CC,Subject,Description):
    Chromeoption.add_argument("--disable-blink-features=AutomationControlled")
    Chromeoption.add_argument(f"--user-data-dir={Mail_Directory}")
    Chromeoption.add_argument('--disable-notifications')
    Chromeoption.add_argument('--disable-popup-blocking')


    prefs = {
        'safebrowsing.enabled': True
    }
    Chromeoption.add_experimental_option('prefs', prefs)
    Driver = webdriver.Chrome(options=Chromeoption)
    Gmail_URL = "https://mail.google.com/mail/u/0/?ogbl#inbox"
    Driver.get(Gmail_URL)
    Driver.maximize_window()
    Web_wait = WebDriverWait(Driver, 20)
    try:
        Web_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Email or phone']"))).send_keys(f'{Email}')    
        Web_wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))).click()
        Web_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Enter your password']"))).send_keys(f'{Password}')
        Web_wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Next']"))).click()
        Web_wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Not now']"))).click()
    except:
        pass
    Web_wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Compose')]"))).click()
    Web_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@peoplekit-id='BbVjBd']"))).send_keys(Send_TO)
    Actions = AC(Driver)
    Actions.send_keys(Keys.ENTER).perform()
    time.sleep(4)

    Web_wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(@aria-label,'Add Cc recipients')]"))).click()
    Web_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@peoplekit-id='BbVjBd']"))).send_keys(Send_CC)
    Web_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name= 'subjectbox']"))).send_keys(Subject)
    Web_wait.until(EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Message Body']"))).send_keys(Description)
    Web_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space() = 'Send']"))).click()    
    time.sleep(4)


Gmail_Login(Mail_Directory="C:/SELENIUM/GMAIL",Email="dataengineeravmb@gmail.com",Password="Alhamdulillah",
            Send_TO="azharbasha25@gmail.com",Send_CC="azharbasha25@gmail.com",
            Subject="TEST MAIL FOR SELENIUM",Description='Hi This is Selenium Projects')