import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

screenshots = '../Screenshot/'


@pytest.fixture(scope = 'function')
def driver():
	driver = webdriver.Chrome()
	driver.get("http://localhost")
	yield driver
	driver.quit()


@pytest.fixture(scope = 'function')
def session():
	return requests.Session()


@pytest.mark.parametrize('q, img, msg', [
	('小米', 'test_search_001.png', '小米手机5'),
	('', 'test_search_002.png', '请输入搜索词'),
	('mihoyo', 'test_search_003.png', '抱歉没找到您要搜索的商品，换个条件试试！'),
])
def test_search_001(driver, session, q, img, msg):
	driver.implicitly_wait(10)
	driver.find_element(By.ID, 'q').send_keys(q)
	driver.find_element(By.CLASS_NAME, 'ecsc-search-button').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + img)
	shiji = driver.find_element(By.TAG_NAME, 'body').text
	assert msg in shiji
