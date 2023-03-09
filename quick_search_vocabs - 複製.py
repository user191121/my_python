vocab1 = input('1,')
vocab2 = input('2,')
vocab3 = input('3,')
vocab4 = input('4,')
vocab5 = input('5,')
vocab_list = [vocab1,vocab2,vocab3,vocab4,vocab5]    # get the vocabs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time 
path = 'C:/Users/albertfu\OneDrive - SKH Holy Trinity Church Secondary School/桌面/chromedriver.exe'
driver = webdriver.Chrome(path) 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(path,options=options)     #import all the helpers and set up fundaments

driver.get('https://dictionary.cambridge.org/')     # visit the site

def search(vocab):      #define searching progress
    search_bar = driver.find_element(By.XPATH, "//input[@id='searchword']")
    search_bar.send_keys(str(vocab))
    search_bar.send_keys(Keys.RETURN)
    print(vocab +"'s meaning are shown below")

def get_trans_text():   #define get trans. text progress
    trans = driver.find_elements(By.CSS_SELECTOR, ".trans.dtrans.dtrans-se.break-cj")
    for tran in trans:
        print(tran.text)
    
def delete():       #define delete progress
    delete_bar = driver.find_element(By.XPATH, "//i[@title='Clear search']")
    delete_bar.click()

counter = 0     #to loop
for i in range(5):
    search(vocab_list[counter])
    get_trans_text()
    delete()
    counter += 1

time.sleep(3)
driver.quit()
    

    

