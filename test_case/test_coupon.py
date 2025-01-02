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


@pytest.mark.parametrize('name, value, consume, num, img, msg', [
	('圣诞冬日礼物', '1225', '2024', '20', 'test_coupon_001.png', '圣诞冬日礼物'),
	('圣诞冬日礼物', '1225', '2024', '20', 'test_coupon_002.png', '已有相同类型的优惠券名称'),
	('', '1225', '2024', '20', 'test_coupon_003.png', '优惠券名称必须'),
	('圣诞冬日礼物', '', '2024', '20', 'test_coupon_004.png', '请填写优惠券面额'),
	('圣诞冬日礼物', '1225', '2024', '', 'test_coupon_005.png', '请填写发放数量'),
])
def test_coupon(driver, session, name, value, consume, num, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[2]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/dl[3]/dt/a/span').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/dl[3]/dd/ul/li[5]/a').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/a/div/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[1]/dd/input').send_keys(name)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/input').send_keys(value)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[3]/dd/input').send_keys(consume)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/input').send_keys(num)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
