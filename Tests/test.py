# -*- coding: utf8 -*-
import json
#to run allure go to terminal to Test dir and send   python -m pytest Tests/test.py --alluredir=c:\Temp
import pytest
from appium import webdriver
from ScreenObjects.SendMessage import SendMsg
import unittest
import allure

@allure.story('Test Automation Solution - Andrei K.')
@allure.feature('Test -  Automation Freamework in Python')
@allure.testcase('Send Message to Olga Test Case')
class AppTestAppium(unittest.TestCase):

  def setUp(self):
      #with open('../Data/data.json', encoding='utf-8') as data_file: #без аллюра
      with open('Data/data.json', encoding='utf-8') as data_file: # с аллюром
          data = json.loads(data_file.read())
      with allure.step("Launch Telegtam"):
          desired_caps = {}
          desired_caps['platformName'] = data['platformName']
          desired_caps['platformVersion'] = data['platformVersion']
          desired_caps['deviceName'] = data['deviceName']
          desired_caps['appPackage'] = data['appPackage']
          desired_caps['appActivity'] = data['appActivity']
          desired_caps['noReset'] = data['noReset']
          self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

  def tearDown(self):
      "Tear down the test"

      self.driver.quit()


  def test_send_messge_to_olga(self):
      "Test is sending message"

      send_message = SendMsg(self.driver)
      send_message.chooseContact()
      send_message.typeMsg()
      #send_message.clickSend()

if __name__ == '__main__':
    unittest.main()