from time import sleep

import yaml
from selenium import webdriver

# 获取cookie值
from selenium.webdriver.common.by import By


def test_get_cookie():
    # 复用浏览器
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    # 获取cookie
    cookies = driver.get_cookies()
    # 写入yaml文件
    with open('data.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(cookies, f)


def test_login():
    driver = webdriver.Chrome()
    # 设置隐形等待
    driver.implicitly_wait(10)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    # 获取cookie值
    with open('data.yaml', encoding='utf-8') as f:
        yaml_cookie = yaml.safe_load(f)
    for cookies in yaml_cookie:
        driver.add_cookie(cookies)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    # 点击首页添加成员
    driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()
    driver.find_element_by_id('username').send_keys('test_1')
    driver.find_element_by_id('memberAdd_acctid').send_keys('test_a')
    driver.find_element_by_id('memberAdd_phone').send_keys('11111111111')
    driver.find_element(By.XPATH, '//*[@class="member_edit_item_right"]').click()
    driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()
    sleep(3)
    driver.quit()
