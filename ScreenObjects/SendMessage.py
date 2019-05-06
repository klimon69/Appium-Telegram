from ScreenObjects.Locators import Locator

class SendMsg(object):

    def __init__(self, driver):
        self.driver = driver
        # try:
        #     self.contactItem = driver.find_element_by_xpath("//android.view.ViewGroup[contains(@index,'2')]")
        #     self.elementTypeField = driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'1')]")
        #     self.sendButton = driver.find_element_by_xpath("//android.widget.ImageView[@content-desc ='Send']")
        #     #self.message = Locator.message
        # except:
        #     print('pidor')

    def chooseContact(self):
        ci = self.driver.find_element_by_xpath("//android.view.ViewGroup[contains(@index,'2')]")
        ci.click()

    def typeMsg(self):
        #self.elementTypeField.clear()
        el = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'1')]")
        el.send_keys("Hello")

    def clickSend(self):
        sb = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc ='Send']")
        sb.click()


