"""
Тест для Simple Form Demo
Сайт: https://the-internet.herokuapp.com/ (локальная копия формы)
Задача: ввести значения в Single Input Field и Two Input Fields,
нажать кнопки и сравнить результаты.
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver() -> webdriver.Chrome:
    """Настройка и запуск драйвера Chrome"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def test_single_input(driver: webdriver.Chrome) -> None:
    """Тестирует блок Single Input Field"""
    print("\n=== Single Input Field ===")
    
    input_field = driver.find_element(By.ID, "single-input")
    input_field.clear()
    input_field.send_keys("Hello Selenium")
    print("  Введено: Hello Selenium")
    
    show_button = driver.find_element(By.ID, "show-btn")
    show_button.click()
    print("  Кнопка 'Show Message' нажата")
    
    result = driver.find_element(By.ID, "display-message").text
    print(f"  Отображено: {result}")
    
    assert result == "Hello Selenium", \
        f"Ошибка: ожидалось 'Hello Selenium', получено '{result}'"
    print("  Результат: ТЕСТ ПРОЙДЕН")


def test_two_inputs(driver: webdriver.Chrome) -> None:
    """Тестирует блок Two Input Fields"""
    print("\n=== Two Input Fields ===")
    
    input_a = driver.find_element(By.ID, "input-a")
    input_a.clear()
    input_a.send_keys("15")
    print("  Введено A: 15")
    
    input_b = driver.find_element(By.ID, "input-b")
    input_b.clear()
    input_b.send_keys("27")
    print("  Введено B: 27")
    
    sum_button = driver.find_element(By.ID, "sum-btn")
    sum_button.click()
    print("  Кнопка 'Get Total' нажата")
    
    total = driver.find_element(By.ID, "sum-result").text
    print(f"  Сумма: {total}")
    
    assert int(total) == 42, \
        f"Ошибка: ожидалось 42, получено '{total}'"
    print("  Результат: ТЕСТ ПРОЙДЕН")


def main() -> None:
    """Основная функция: запуск браузера и тестов"""
    driver = setup_driver()
    
    try:
        # Открываем локальную HTML-форму
        html_path = os.path.abspath("form.html")
        driver.get(f"file://{html_path}")
        print("Страница загружена")
        
        # Запуск тестов
        test_single_input(driver)
        test_two_inputs(driver)
        
        print("\n" + "=" * 40)
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО")
        print("=" * 40)
        
    finally:
        driver.quit()
        print("\nБраузер закрыт")


if __name__ == "__main__":
    main()