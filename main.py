import yaml
import time
import pyperclip
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

# 설정 파일 읽기
def read_config(file_path):
    # setting.yml 파일 경로
    yaml_file = file_path

    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    return data

# Login
def naver_login(id, pw):
    ctrl_key = Keys.CONTROL
    if platform.system() == 'Darwin':
        ctrl_key = Keys.COMMAND

    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com')
    time.sleep(1)

    id_selector = '#id'
    pw_selector = '#pw'
    login_btn_selector = '#log\.login'

    # id 입력
    id_input = driver.find_element(By.CSS_SELECTOR, id_selector)
    id_input.click()
    time.sleep(1)
    pyperclip.copy(id)
    time.sleep(1)
    ActionChains(driver).key_down(ctrl_key).send_keys('v').key_down(ctrl_key).perform()
    
    time.sleep(2)

    # pw 입력
    pw_input = driver.find_element(By.CSS_SELECTOR, pw_selector)
    pw_input.click()
    time.sleep(1)
    pyperclip.copy(pw)
    time.sleep(1)
    ActionChains(driver).key_down(ctrl_key).send_keys('v').key_down(ctrl_key).perform()

    # login button click
    login_btn = driver.find_element(By.CSS_SELECTOR, login_btn_selector)
    login_btn.click()


# FeedList 화면 출력
def get_feed_list():
    driver.get('http://m.blog.naver.com/FeedList.naver')

if __name__ == "__main__":
    config_data = read_config('setting.yml')

    naver_login(config_data['naver']['id'], config_data['naver']['pw'])

    time.sleep(1)

    get_feed_list()

    input()

    


