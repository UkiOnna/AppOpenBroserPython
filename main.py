import bs4
import requests
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://kurs.kz")
pricesForBuy=[]
pricesForSell=[]
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
buy= soup.find_all('span',attrs = {'title' : 'USD - покупка'})
for x in buy:
    pricesForBuy.append(x.text)
sell=soup.find_all('span',attrs = {'title' : 'USD - продажа'})
for x in sell:
    pricesForSell.append(x.text)

driver.get('https://mail.protonmail.com/')

auth = driver.find_element_by_name('username')
auth.send_keys('')

auth = driver.find_element_by_name('password')
auth.send_keys('password')

auth.send_keys(Keys.RETURN)
