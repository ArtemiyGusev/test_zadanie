import time
from selenium import webdriver
import requests
class b():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options)
        perehod = driver.get("https://shop.salonsecret.ru/")
        print("Переход на https://shop.salonsecret.ru/ успешен")
    except Exception as e:
        print("Ошибка Webdriver" + e)

def login():
    b.driver.implicitly_wait(10)
    loginx = b.driver.find_element_by_xpath('//*[@class="HeaderAccount_text__2vV2l"][contains(text(),"Вход")]').click()
def vvod_email():
    b.driver.implicitly_wait(10)
    vvod_emailx = b.driver.find_element_by_xpath('//*[@class="Field_input__3Qu2w"][@name="email"]').send_keys("artjom9useff@yandex.ru")

def vvod_password():
    b.driver.implicitly_wait(10)
    vvod_passwordx = b.driver.find_element_by_xpath('//*[@class="Field_input__3Qu2w"][@name="password"]').send_keys("A121212a")

def knopkivhod_click(index):
    b.driver.implicitly_wait(10)
    knopkivhod_clickx = b.driver.find_elements_by_xpath('//*[@class="Button_button__3uOSp LoginForm_loginSubmit__1MUVl Button_primary__1-9aR"][contains(text(),"Войти")]')[index].click()
    b.driver.implicitly_wait(10)
def logintest():
    try:
        login()
        time.sleep(1)
        vvod_email()
        time.sleep(1)
        vvod_password()
        time.sleep(1)
        knopkivhod_click(index=0)
    except Exception as e:
        print(e)

logintest()

