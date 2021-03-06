from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self, base_url)
        self.soap = SoapHelper(self, base_url)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//form[@name='MainForm']//div[1]//input[1]")) > 0:
            return
        wd.get(self.base_url)
        
        
    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()


    