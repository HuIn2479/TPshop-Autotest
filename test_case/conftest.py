import json

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_cookies(driver, cookie_file = 'cookie.json'):
	driver.implicitly_wait(10)
	driver.delete_all_cookies()
	with open(cookie_file, 'r') as f:
		cookies = json.loads(f.read())
		for cookie in cookies:
			driver.add_cookie(cookie)
	driver.refresh()


@pytest.fixture(scope = 'function')
def load_admin(driver):
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[1]/input').send_keys('admin')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[2]/input').send_keys('123456')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[3]/input').send_keys('8888')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[5]/span/input').click()

@pytest.fixture(scope = 'function')
def driver(request):
	url = request.param if hasattr(request, 'param') else "http://localhost"
	driver = webdriver.Chrome()
	driver.get(url)
	yield driver
	driver.quit()


@pytest.fixture(scope = 'function')
def session():
	return requests.Session()
