from autotesting.qqq import *

def korzina_click():
    b.driver.implicitly_wait(5)
    korzina_clickx = b.driver.find_element_by_xpath('//*[@class="CartLink_root__1h6W_"]').click()

def kpokupkam_click():
    b.driver.implicitly_wait(5)
    kpokupkam_clickx = b.driver.find_element_by_xpath('//*[@class="Button_button__3uOSp Button_primary__1-9aR"][contains(text(),"К покупкам")]').click()

def vkorziny_tovar_click(index):
    b.driver.implicitly_wait(5)
    vkorziny_tovar_clickx = b.driver.find_elements_by_xpath('//*[@class="ProductGridItem_finalPrice__19zXZ"]')[index].click()


def plus_kolvo_tovar_vkorzine():
    b.driver.implicitly_wait(5)
    plus_kolvo_tovar_vkorzinex = b.driver.find_element_by_xpath('//*[@d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"]').click()


def minus_kolvo_tovar_vkorzine():
    b.driver.implicitly_wait(5)
    minus_kolvo_tovar_vkorzinex = b.driver.find_element_by_xpath('//*[@d="M0 7v2h8V7z"]').click()


def dobavit_tovar_vkorziny():
    b.driver.implicitly_wait(5)
    dobavit_tovar_vkorzinyx = b.driver.find_element_by_xpath('//*[@class="Button_button__3uOSp Button_primary__1-9aR"][contains(text(),"Добавить в корзину")]').click()

def perehod_vkorziny():
    b.driver.implicitly_wait(5)
    perehod_vkorzinyx = b.driver.find_element_by_xpath('//*[@class="Button_button__3uOSp Button_borderless__3DPYR"][contains(text(),"В корзину")]').click()


def proverka_kolvo_tovara():
    b.driver.implicitly_wait(5)
    proverka_kolvo_tovarax = b.driver.find_element_by_xpath('//*[@class="Cart_qtyInput__Xh20f"][@value="3"]')

print('Выполнение TestCase: CartCestUpd')
try:
    korzina_click()
    time.sleep(1)
    kpokupkam_click()
    vkorziny_tovar_click(index=0)
    chetchik = 0
    while True:
        chetchik = chetchik + 1
        time.sleep(1)
        plus_kolvo_tovar_vkorzine()
        if chetchik == 5:
            break
    dobavit_tovar_vkorziny()
    time.sleep(1)
    perehod_vkorziny()

    while True:
        chetchik = chetchik - 1
        time.sleep(1)
        minus_kolvo_tovar_vkorzine()
        if chetchik == 2:
            break
    b.driver.refresh()

    proverka_kolvo_tovara()

    print('Успех TestCase: CartCestUpd')
except Exception as e:
    print('Провал TestCase: CartCestUpd')