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

# @pytest.mark.parametrize('driver', ["http://localhost/index.php/Admin/Index/index"], indirect=True)
@pytest.mark.parametrize('name, detailed, phone, img, msg', [
	('1cn', '花海大盗', '170522', 'test_selfpickup_001.png', '1cn'),
	('', 'yc', '170522', 'test_selfpickup_002.png', '自提点名称不能为空'),
	('1cn', '', '170522', 'test_selfpickup_003.png', '请填写地址'),
])
def test_selfpickup(driver, session, name, detailed, phone, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[1]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/dl[1]/dd/ul/li[7]/a').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div/a/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[1]/dd/input').send_keys(name)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[1]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[1]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[2]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dt/label').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[3]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/select[3]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[3]/dd/select').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[3]/dd/select/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/textarea').send_keys(detailed)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[6]/dd/input').send_keys(phone)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
