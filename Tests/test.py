import unittest
from appium import webdriver
from ScreenObjects.SendMessage import SendMsg


class AppTestAppium(unittest.TestCase):

  def setUp(self):
      desired_caps = {}
      desired_caps['platformName'] = 'Android'
      desired_caps['platformVersion'] = ''
      desired_caps['deviceName'] = '81e9b20e'
      desired_caps['appPackage'] = 'org.telegram.messenger'
      desired_caps['appActivity'] = 'org.telegram.ui.LaunchActivity'
      desired_caps['noReset'] = 'True'
      self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

  def tearDown(self):
      "Tear down the test"

      self.driver.quit()


  def test_send_messge_to_olga(self):
      "Test is sending message"

      send_message = SendMsg(self.driver)
      send_message.chooseContact()
      send_message.typeMsg()
      send_message.clickSend()


      # contactItem = self.driver.find_element_by_xpath("//android.view.ViewGroup[contains(@index,'2')]")
      # contactItem.click()
      # elementTypeField = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'1')]")
      # elementTypeField.clear()
      # elementTypeField.send_keys("Hello. If you are reading this, my first appium automation has passed")
      # sendButton = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc ='Send']")
      # sendButton.click()



if __name__ == '__main__':
    unittest.main()