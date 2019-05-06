from ScreenObjects.Locators import Locator

class SendMsg(object):

    def __init__(self, driver):
        self.driver = driver

    def chooseContact(self):
        self.contactItem = Locator.contactItem
        contact = self.driver.find_element_by_xpath(self.contactItem)
        contact.click()

    def typeMsg(self):
        self.elementTypeField = Locator.elementTypeField
        self.message = Locator.message
        inputField = self.driver.find_element_by_xpath(self.elementTypeField)
        inputField.clear()
        inputField.send_keys(self.message)

    def clickSend(self):
        self.sendButton = Locator.sendButton
        sendBtn = self.driver.find_element_by_xpath(self.sendButton)
        sendBtn.click()


