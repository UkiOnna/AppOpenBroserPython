import bs4
import requests
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://kurs.kz")
text=''
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
buy= soup.find_all('span',attrs = {'title' : 'USD - покупка'})
text+="BUY\n"
for x in buy:
    text+=x.text+'\n'
sell=soup.find_all('span',attrs = {'title' : 'USD - продажа'})
text+="SELL"
for x in sell:
    text+=x.text+'\n'

print(text)
driver.get('https://mail.ru/')
time.sleep(2)
auth = driver.find_element_by_id('mailbox:login')

auth.send_keys('uk1onna@mail.ru')

python_button = driver.find_elements_by_xpath("//input[@class='o-control' and @value='Ввести пароль']")[0]
python_button.click()
time.sleep(1)
password = driver.find_element_by_id('mailbox:password')
password.send_keys('1765mail')
python_button = driver.find_elements_by_xpath("//input[@class='o-control' and @value='Ввести пароль']")[0]
python_button.click()
time.sleep(40)

python_button = driver.find_elements_by_class_name("sidebar__compose-btn-box")[0]
python_button.click()
time.sleep(10)
inputWho=driver.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input")
inputWho.send_keys('Zhauzhurek@bk.ru')

inputWho=driver.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/input")
inputWho.send_keys('Sikirov.T')

inputWho=driver.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]")
inputWho.send_keys(text)

sendB=driver.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]/span/span")
sendB.click()
auth.send_keys(Keys.RETURN)
time.sleep(5)
