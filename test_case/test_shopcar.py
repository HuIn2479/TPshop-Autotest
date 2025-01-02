import json
import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

screenshots = '../Screenshot/'


def load_cookies(driver, cookie_file = 'cookie.json'):
	driver.delete_all_cookies()
	with open(cookie_file, 'r') as f:
		cookies = json.loads(f.read())
		for i in cookies:
			driver.add_cookie(i)
	driver.refresh()


@pytest.fixture(scope = 'function')
def driver():
	driver = webdriver.Chrome()
	driver.get('http://localhost/')
	yield driver
	driver.quit()


@pytest.fixture(scope = 'function')
def session():
	return requests.Session()


def test_shopcar_001(driver, session):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/a/div/span').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_shopcar_001.png')
	current_url = driver.current_url
	assert 'localhost/Home/Cart/index.html' in current_url


def test_shopcar_002(driver,session):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/a[3]').click()
	driver.find_element(By.XPATH, '//*[@id="join_cart"]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH,'/html/body/div[11]/span/a').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/a/div').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_shopcar_002.png')
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	msg = '小米手机5,十余项黑科技，很轻狠快'
	assert msg in shiji


def test_shopcar_003(driver, session):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/a[2]').click()
	number = driver.find_element(By.XPATH, '//*[@id="number"]')
	driver.execute_script("arguments[0].value = '';", number)
	driver.find_element(By.XPATH, '//*[@id="number"]').send_keys('3')
	driver.find_element(By.XPATH, '//*[@id="join_cart"]').click()
	time.sleep(5)
	driver.find_element(By.XPATH, '/html/body/div[11]/span/a').click()
	driver.implicitly_wait(20)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/a/div').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_shoppingcar_003.png')
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	msg = '原封国行【优惠套餐】Apple/苹果 iPhone 6s 4.7英寸 4G手机'
	assert msg in shiji
