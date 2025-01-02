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


@pytest.mark.parametrize('name, number, detailed, img, msg', [
	('雷', '13200530000', '花海大到', 'test_order_001.png', '小米15'),
	('', '13200530000', '花海大到', 'test_order_002.png', '请填写收货人'),
	('米', '', '花海大到', 'test_order_003.png', '收货人联系电话'),
	('某某', '13200530000', '', 'test_order_004.png', '请填写详细地址'),

])
def test_order(driver,session, name, number, detailed, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[2]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/dl[2]/dt/a/span').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[2]/a/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/input').send_keys(name)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[3]/dd/input').send_keys(number)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[1]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[1]/option[2]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[2]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/input').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[2]/option[2]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[3]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/select[3]/option[2]').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/input').send_keys(detailed)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[8]/dd/a').click()
	driver.implicitly_wait(10)
	iframe = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/i').click()
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div/div/input').click()
	driver.implicitly_wait(10)
	driver.switch_to.default_content()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
