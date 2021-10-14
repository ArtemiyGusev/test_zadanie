import time
from selenium import webdriver
import unittest



class b():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options)
        perehod = driver.get("https://shop.salonsecret.ru/")
        print("Переход на https://shop.salonsecret.ru/ успешен")
    except Exception as e:
        print("Ошибка Webdriver")


def registracia_click():
    b.driver.implicitly_wait(5)
    registracia_clickx = b.driver.find_element_by_xpath('//*[@class="HeaderAccount_text__2vV2l"][contains(text(),"Регистрация")]').click()


#Проверяем что в поле номера телефона корректная маска телефона
def test_pole_nomer_tel():
    b.driver.implicitly_wait(5)
    pole_nomer_telx = b.driver.find_element_by_xpath('//input[@name="telephone"][@value]')
    pole_nomer_telx.send_keys("7")
    proverka_maski_tel = pole_nomer_telx.get_attribute('value')
    try:
        assert proverka_maski_tel == '+7 (___) ___ __ __'
        print('Маска в поле номера телефона корректна')
    except Exception:
        print('Маска номера телефона не совпадает с ожидающим результатом')


#Тест по проверке введенего номера телефона в поле
def test_vvod_nomer_tel():
    b.driver.implicitly_wait(5)
    vvod_nomer_telx = b.driver.find_element_by_xpath('//input[@name="telephone"][@value]')
    vvod_nomer_telx.send_keys('9453969889')
    proverka_vvoda_tel = vvod_nomer_telx.get_attribute('value')
    try:
        assert proverka_vvoda_tel == '+7 (945) 396 98 89'
        print('Номер телефона корректный')
    except Exception:
        print('Номер телефона не совпадает с ожидающим результатом')


class TestCaseMaskTel(unittest.TestCase):
    try:
        b()
        registracia_click()
        test_pole_nomer_tel()
        time.sleep(1)
        test_vvod_nomer_tel()
        print('TestCaseMaskTel - Выполнен успешно')
    except Exception:
        print('TestCaseMastTel - Провал')