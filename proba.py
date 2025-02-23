from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Найти текстовое поле и ввести ответ
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # Переключить radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)  # Прокрутка к элементу
    time.sleep(13)
    radiobutton.click()

    # Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)  # Прокрутка к кнопке
    submit_button.click()

    # Ждем несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрыть браузер после выполнения
    browser.quit()


