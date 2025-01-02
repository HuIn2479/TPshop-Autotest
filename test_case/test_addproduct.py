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


@pytest.mark.parametrize('name, price, mprice, img, msg', [
	('小米15', '4000', '4490', 'test_addproduct_001.png', '操作成功'),
	('', '4000', '4490', 'test_addproduct_002.png', '商品名称必填'),
	('小米15', '', '4490', 'test_addproduct_003.png', '本店售价必须'),
	('小米16', '4090', '', 'test_addproduct_004.png', '市场价格必填'),
	('小米17', '1111', '5', 'test_addproduct_005.png', '市场价不得小于本店价'),
])
def test_addproduct(driver, session, name, price, mprice, img, msg):
	driver.implicitly_wait(10)
	load_cookies(driver)
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[2]/a').click()
	iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/iframe')
	driver.switch_to.frame(iframe)
	driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/a/div/span').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[1]/dd/input').send_keys(name)
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[1]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[1]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[2]/option[2]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[3]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[6]/dd/select[3]/option[3]').click()
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[9]/dd/input').send_keys(price)
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/dl[10]/dd/input').send_keys(mprice)
	driver.find_element(By.XPATH, '/html/body/div[3]/form/div[6]/div/a').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
