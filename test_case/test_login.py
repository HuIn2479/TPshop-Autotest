import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

screenshots = '../Screenshot/'


@pytest.fixture(scope = 'function')
def driver():
	driver = webdriver.Chrome()
	driver.get('http://localhost')
	yield driver
	driver.quit()


@pytest.mark.parametrize('username, password, verify_code, img, msg', [
	('15600000000', '0987654321', '8888', 'test_login_001.png', '安全退出'),
	('12000000000', '0987654321', '8888', 'test_login_002.png', '账号不存在'),
	('', '0987654321', '8888', 'test_login_003.png', '用户名不能为空'),
	('15600000000', '', '8888', 'test_login_004.png', '密码不能为空'),
	('15600000000', '0987654321', '', 'test_login_005.png', '验证码不能为空'),
	('15600000000', 'ainiyahihi', '8888', 'test_login_006.png', '密码错误'),
	('ainiya', '0987654321', '8888', 'test_login_007.png', '账号格式不匹配'),
	('15600000000', '0987654321', '喵', 'test_login_008.png', '验证码错误'),
	('', '', '', 'test_login_010.png', '用户名不能为空')
])
def test_login(driver, session, username, password, verify_code, img, msg):
	driver.implicitly_wait(10)
	login = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
	login.click()
	username_field = driver.find_element(By.ID, 'username')
	password_field = driver.find_element(By.ID, 'password')
	verify_code_field = driver.find_element(By.ID, 'verify_code')
	username_field.send_keys(username)
	password_field.send_keys(password)
	verify_code_field.send_keys(verify_code)
	regbtn = driver.find_element(By.NAME, 'sbtbutton')
	regbtn.click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
	driver.quit()
