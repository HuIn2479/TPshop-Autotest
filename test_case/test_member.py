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


@pytest.mark.parametrize('name, pd, num, em, img, msg', [
	('1ch', '0987654321', '18200010086', 'me@example.cn', 'test_vip_001.png', '1ch'),
	('', '0987654321', '18200010086', 'me@example.cn', 'test_vip_002.png', '昵称不能为空'),
	('2no', '', '18200010086', 'me@example.cn', 'test_vip_003.png', '密码不能为空 密码长度不正确'),
	('3ip', '098', '18200010086', 'me@example.cn', 'test_vip_004.png', '密码长度不正确'),
	('4power', '0987654321', '', '', 'test_vip_005.png', '手机和邮箱请至少填一项'),
])
def test_vip(driver, session, name, pd, num, em, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[1]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/dl[2]/dt/a/span').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/a/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[1]/dd/input').send_keys(name)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[2]/dd/input').send_keys(pd)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[3]/dd/input').send_keys(num)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/dl[4]/dd/input').send_keys(em)
	driver.find_element(By.XPATH, '/html/body/div[4]/form/div/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
