import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

screenshots = '../Screenshot/'


def load_cookies(driver):
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[1]/input').send_keys('admin')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[2]/input').send_keys('123456')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[3]/input').send_keys('8888')
	driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[5]/span/input').click()


@pytest.fixture(scope = 'function')
def driver():
	driver = webdriver.Chrome()
	driver.get('http://localhost/index.php/Admin/Index/index')
	yield driver
	driver.quit()


@pytest.fixture(scope = 'function')
def session():
	return requests.Session()


@pytest.mark.parametrize('name, price, item, xu, img, msg', [
	('小米15', '10', '1', '1', 'test_buy_001.png', '小米15'),
	('', '10', '1', '1', 'test_buy_002.png', '团购标题必须'),
	('小米15', '', '1', '1', 'test_buy_003.png', '请填写团购价格'),
	('小米15', '10', '', '1', 'test_buy_004.png', '请填写参加团购数量'),
])
def test_buy(driver, session, name, price, item, xu, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[2]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/dl[3]/dt/a/span').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/dl[3]/dd/ul/li[2]/a').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/a/div/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[1]/dd/input').send_keys(name)
	driver.implicitly_wait(20)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/p/a').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/input').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div[5]/a').click()
	driver.switch_to.parent_frame()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[5]/dd/input[1]').send_keys(price)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[6]/dd/input').send_keys(item)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[7]/dd/input').send_keys(xu)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
