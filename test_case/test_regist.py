import time

import pytest
from selenium.webdriver.common.by import By

screenshots = '../Screenshot/'


@pytest.mark.parametrize('username, yanzhengma, password, confirm_password, img, msg', [
	('15600000000', '8888', 'cy123456', 'cy123456', 'resign_001.png', '17708'),
	('15600000000', '8888', 'cy123456', 'cy123456', 'resign_002.png', '账号已存在'),
	('', '8888', 'cy123456', 'cy123456', 'resign_003.png', '请用手机号或邮箱注册'),
	('me@qq.com', '8888', 'cy123456', 'cy123456', 'resign_004.png', '请用手机号或邮箱注册')
])
def test_resign(driver,session, username, yanzhengma, password, confirm_password, img, msg):
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/a[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div/div/div/div[1]/div/input').send_keys(username)
	driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div/div/div/div[2]/div[1]/input').send_keys(yanzhengma)
	driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div/div/div/div[3]/div/input').send_keys(password)
	driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div/div/div/div[4]/div/input').send_keys(confirm_password)
	driver.find_element(By.XPATH, '//*[@id="reg_form2"]/div/div/div/div[6]/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji