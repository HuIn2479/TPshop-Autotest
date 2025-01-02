import json
import time
import pytest
import requests
from selenium import webdriver
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
	driver.get("http://localhost")
	yield driver
	driver.quit()


@pytest.fixture(scope = 'function')
def session():
	return requests.Session()


def test_address_001(driver, session):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/a[1]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/ul[4]/li[4]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div[1]/a/span').click()
	driver.implicitly_wait(10)
	iframe = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[1]/td[2]/input').send_keys('10721')
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[1]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[1]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[2]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[2]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[3]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/select[3]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/textarea').send_keys(
		'haha')
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[5]/td[2]/input').send_keys(
		'13200000721')
	driver.find_element(By.XPATH, '/html/body/div/div/div/form/table/tbody/tr[6]/td[2]/button/span').click()
	time.sleep(5)
	driver.switch_to.parent_frame()
	driver.save_screenshot(screenshots + 'test_address_001.png')
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	msg = '10721'
	assert msg in shiji

