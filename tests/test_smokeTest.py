import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class TestSmokeTest:
  def setup_method(self, method):
    options = Options()
    options.add_argument('--headless')
    self.driver = webdriver.Firefox(options=options)
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homePage1(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1256, 1032)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/admin.html")
    self.driver.set_window_size(1164, 1032)
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("BobBobber")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Bobby")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/directory.html")
    self.driver.set_window_size(1280, 800)
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_homePage2(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1280, 800)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    self.vars["currentUrl"] = self.driver.execute_script("return window.location.href;")
    assert(self.vars["currentUrl"] == "http://127.0.0.1:5500/teton/1.6/join.html")
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/join.html")
    self.driver.set_window_size(1280, 800)
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Bob")
    self.driver.find_element(By.NAME, "lname").click()
    self.driver.find_element(By.NAME, "lname").send_keys("Bobberton")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Bobs Bobbers")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Owner")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
