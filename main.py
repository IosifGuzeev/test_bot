from selenium import webdriver
import re
import pandas as pd
data = pd.read_csv('data.csv')

login = "guzeev98@gmail.com"
password = "das123FAS"

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

id = driver.find_element_by_xpath("//input[@type='radio']").get_attribute("name")
print(id)
options = driver.find_elements_by_xpath("//div[@class='r0']")
options.extend(
    driver.find_elements_by_xpath("//div[@class='r1']")
)
q_text = driver.find_element_by_class_name("qtext").text
print(q_text)
right_answ_ind = 0
string = data[data['question'].str.contains(q_text)].iloc[0]['answer_text']
print(string)
for option in options:
    html = option.get_attribute('innerHTML')
    answer_id = re.findall("answer[0-9]", html)[0][-1]
    answer_text = re.findall(r"<em>.+<\/em>", html)[0][4:-5]

    answer_text = re.sub(r'<a.[^>]+>|</a>|</em>|<em>', '', answer_text)
    print(string)
    print(answer_text)
    if answer_text.find(string) != -1:
        print(right_answ_ind)
        break
    else:
        print(answer_text.find(string))
        right_answ_ind += 1

radio_btn_0 = driver.find_element_by_id(f"{id}{right_answ_ind}")
radio_btn_0.click()
