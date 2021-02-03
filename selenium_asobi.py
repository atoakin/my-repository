from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

USERNAME=""#個人情報なので伏せました
PASSWORD =""#同じく伏せました

driver = webdriver.Chrome()
error_flg=False
target_url="https://www.instagram.com"
driver.get(target_url)
sleep(3)

if error_flg == False:
    try:
        username_input= driver.find_element_by_xpath('//input[@aria-label="電話番号、ユーザーネーム、メールアドレス"]')
        username_input.send_keys(USERNAME)
        sleep(1)

        password_input=driver.find_element_by_xpath('//input[@aria-label="パスワード"]')
        password_input.send_keys(PASSWORD)
        sleep(1)

        username_input.submit()
        sleep(4)

        notnow_button= driver.find_element_by_xpath('//button[contains(text()="後で")]')
        notnow_button.click()
        sleep(1)

        notnow_button= driver.find_element_by_xpath('//button[contains(text()="後で")]')
        notnow_button.click()
        sleep(1)

    except Exception:
        error_flg=True
        print("ログインボタン押下時にエラーが発生しました。")

target_username="ikutaerika.official"
if error_flg is False:
    try:
        target_profile_url=target_url+"/"+target_username+"/"
        driver.get(target_profile_url)
        sleep(3)

    except Exception:
        error_flg=True
        print("検索時にエラーが発生しました。")
