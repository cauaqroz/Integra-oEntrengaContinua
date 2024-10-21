from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("/index.html")

def test_lance_menor_que_minimo():
    bid_input = driver.find_element(By.ID, "bidValue")
    bid_input.send_keys("50")
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    message = driver.find_element(By.ID, "message")
    assert "O valor do lance deve ser no mínimo R$ 100,00." in message.text

def test_lance_valido():
    bid_input = driver.find_element(By.ID, "bidValue")
    bid_input.clear()
    bid_input.send_keys("150")
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    message = driver.find_element(By.ID, "message")
    assert "Lance de R$ 150 aceito com sucesso!" in message.text

test_lance_menor_que_minimo()
time.sleep(2)
test_lance_valido()
time.sleep(2)

driver.quit()
