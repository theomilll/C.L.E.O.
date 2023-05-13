from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .forms import SignUpForm
from .selPath import SELENIUM_DIRS

class cleo(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(SELENIUM_DIRS, options=chrome_options)

        driver.get("http://127.0.0.1:8000/")
        register = driver.find_element(By.ID,"signUp")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.NAME,"username")
        username_register.send_keys("thanos")
        email_register = driver.find_element(By.NAME,"email")
        email_register.send_keys("thanos@gmail.com")
        password_register = driver.find_element(By.NAME,"password1")
        password_register.send_keys("inevitavel40")
        confirm_register = driver.find_element(By.NAME,"password2")
        confirm_register.send_keys("inevitavel40")
        login = driver.find_element(By.ID,"Sign Up")
        login.click()
        escrever_username = driver.find_element(By.NAME,"Username")
        escrever_username.send_keys("thanos")
        password_login = driver.find_element(By.NAME,"password")
        password_login.send_keys("inevitavel40")
        time.sleep(1)
        botao_login = driver.find_element(By.NAME,"login")
        botao_login.click()
        time.sleep(2)
        adicionar_carrinho = driver.find_element(By.NAME,"cartAdd")
        adicionar_carrinho.click()
        time.sleep(2)
        first_product = driver.find_element(By.NAME, "product-link")
        first_product.click()
        time.sleep(2)
        for i in range(4):
            increase_button = driver.find_element(By.NAME, "increase")
            increase_button.click()
            time.sleep(1)
        for i in range(4):
            decrease_button = driver.find_element(By.NAME, "decrease")
            decrease_button.click()
            time.sleep(1)
        adicionar_carrinho2 = driver.find_element(By.NAME, "cartAdd")
        adicionar_carrinho2.click()
        time.sleep(2)
        # leftArrowBack = driver.find_element(By.NAME, 'go-back')
        # leftArrowBack.click()
        # time.sleep(2)
        cartBtn = driver.find_element(By.NAME, "cart")
        cartBtn.click()
        time.sleep(2)
        for i in range(2):
            cartDecrease = driver.find_element(By.NAME, "decreaseCart")
            cartDecrease.click()
            time.sleep(1)
        for i in range(2):
            cartIncrease = driver.find_element(By.NAME, "increaseCart")
            cartIncrease.click()
            time.sleep(1)
        cartObs = driver.find_element(By.NAME, "text_box_obs")
        cartObs.send_keys("Eu sou inevitavel!")
        time.sleep(2)
        cartObsBtn = driver.find_element(By.NAME, "obsCartBtn")
        cartObsBtn.click()
        time.sleep(2)
        finalizarCompra = driver.find_element(By.NAME, "finalizarCompra")
        finalizarCompra.click()
        time.sleep(2)
        paymentMethod = driver.find_element(By.NAME, 'payment-method')
        paymentMethod.click()
        pixPay = driver.find_element(By.NAME, "pixPay")
        pixPay.click()
        time.sleep(1)
        qrCodeGen = driver.find_element(By.NAME, "generateQrCode")
        qrCodeGen.click()
        time.sleep(3)
        confirmPurchase = driver.find_element(By.NAME, "confirmPurchase")
        confirmPurchase.click()
        time.sleep(1)
        # cartClear = driver.find_element(By.NAME, "clearCart")
        # cartClear.click()
        # time.sleep(2)
        driver.quit()