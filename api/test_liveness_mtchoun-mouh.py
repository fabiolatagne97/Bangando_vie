# Generated by Selenium IDE
import pytest
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestLiveness():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_liveness(self):
    WEBSITE_URL_MAIL_NAMESPACE =  os.environ["WEBSITE_URL_MAIL_NAMESPACE"]

    # Test name: liveness
    # Step # | name | target | value | comment
    
    # 1 | open | / |  | 
    self.driver.get(WEBSITE_URL_MAIL_NAMESPACE)
    # 2 | setWindowSize | 976x1016 |  | 
    self.driver.set_window_size(976, 1016)
    # 3 | click | id=name-input |  | 
    self.driver.find_element(By.ID, "name-input").click()
    # 4 | type | id=name-input | JORDANE TSAFACK  | 
    self.driver.find_element(By.ID, "name-input").send_keys("MONGULU Liveness")
    # 5 | type | id=email-input | jordanetsafack@yahoo.fr | 
    self.driver.find_element(By.ID, "email-input").send_keys("hsk6n.mtchoun-mouh.mongulu-cm.hsk6n@inbox.testmail.app")
    # 6 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 7 | click | css=.col-4 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-4").click()
    time.sleep(5)
  


