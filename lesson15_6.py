import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем страницу с ссылкой
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    
    # Вычисляем текст ссылки по формуле
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    
    # Находим и кликаем по зашифрованной ссылке
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    
    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Копируем код из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    code = alert_text.split(": ")[-1]
    print(f"Код для ответа: {code}")
    
    # Закрываем браузер
    browser.quit()
