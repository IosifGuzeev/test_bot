from selenium import webdriver
import re
import pandas as pd
import numpy as np
import time

login = "guzeev98@gmail.com"
password = "das123FAS"

data = pd.read_csv('new_data_(123).csv')

driver = webdriver.Chrome()
driver.get("https://moodle.tsu.ru/")
login_btn = driver.find_element_by_class_name("btn-login")
login_btn.click()

login_btn = driver.find_element_by_id("login_url")
login_btn.click()

username_box = driver.find_element_by_id("Email")
password_box = driver.find_element_by_id("Password")

username_box.send_keys(login)
password_box.send_keys(password)

login_btn = driver.find_element_by_class_name("btn-success")
login_btn.click()

driver.get("https://moodle.tsu.ru/mod/quiz/view.php?id=51884")
start_btn = driver.find_element_by_xpath("//input[@type='submit']")
start_btn.click()

not_found_count = 0
while True:
    try:
        id = driver.find_element_by_xpath("//input[@type='radio']").get_attribute("name")
    except:
        print("Radio button not found!")
        next_btn = driver.find_element_by_name("next")
        next_btn.click()
        continue
    options = [
        (
            driver.find_element_by_id(str(id) + "0"),
            driver.find_element_by_xpath(f'//label[@for="{id}0"]').text[3:]
        ),
        (
            driver.find_element_by_id(str(id) + "1"),
            driver.find_element_by_xpath(f'//label[@for="{id}1"]').text[3:]
        ),
        (
            driver.find_element_by_id(str(id) + "2"),
            driver.find_element_by_xpath(f'//label[@for="{id}2"]').text[3:]
        ),
        (
            driver.find_element_by_id(str(id) + "3"),
            driver.find_element_by_xpath(f'//label[@for="{id}3"]').text[3:]
        )
    ]

    q_text = driver.find_element_by_class_name("qtext").text.lower()
    right_answ_ind = 0
    try:
        correct_answer = data[data['question'].str.contains(q_text)].iloc[0]['answer_text'].lower()
    except:
        print(f"Question is not found in database.({not_found_count} is not found already)")
        not_found_count += 1
        next_btn = driver.find_element_by_name("next")
        next_btn.click()
        continue
    correct_option = None
    for option in options:
        if option[1].find(correct_answer) != -1:
            correct_option = option
            break
    if correct_option is None:
        next_btn = driver.find_element_by_name("next")
        next_btn.click()
        continue
    correct_option[0].click()
    next_btn = driver.find_element_by_name("next")
    next_btn.click()
    time.sleep(np.random.randint(0, 1))  # Чтобы нас не банили за слишком быстрый ответ
                                        # мы ждем от 1 до 3 секунд после каждого ответа


