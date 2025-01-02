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


def test_carousel_001(driver, session):
	driver.implicitly_wait(10)
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_carousel_001.png')


def test_carousel_002(driver, session):
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[2]/a/img').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_carousel_002.png')


def test_carousel_003(driver, session):
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[2]/a[2]').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_carousel_003.png')

def test_carousel_004(driver, session):
	driver.implicitly_wait(10)
	driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/span[1]').click()
	time.sleep(5)
	driver.save_screenshot(screenshots + 'test_carousel_004.png')

