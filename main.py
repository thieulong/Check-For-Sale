import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from message import send_message

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(chrome_options=options)

with open('config.json') as file:
    config = json.load(file)

status = config["status"]
website_domain = config["website_domain"]
product_link = config["product_link"]
normal_price = config["normal_price"]
telegram_user_id = config["telegram_user_id"]

browser.get(product_link)

product_name = browser.find_element(By.XPATH, '//h1[@class="pdp-jss-productTitle-28"]')
product_name = product_name.text
current_price = browser.find_element(By.XPATH, '//span[@class="pdp-jss-actual-76 pdp-jss-actual-126"]')
current_price = current_price.text

if normal_price > float(current_price):
    save = normal_price - current_price
    message = "[ALERT] {} is currently on sale for only ${}, you can save up to {}! Find out more here: {}".format(product_name, current_price, save, product_link)

elif normal_price == float(current_price):
    message = "[UPDATE] The price of {}is still remains at ${} for today.".format(product_name, current_price)

send_message(user_id=telegram_user_id, msg=message)