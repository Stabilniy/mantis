import time
class SessionHelper:
    
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@class='button']").click()
        time.sleep(3)

    def get_logged_in_name(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_in_name() == username

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))>0

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    #def ensure_login(self, username, password):
    #    wd = self.app.wd
    #    if self.is_logged_in():
    #        if self.is_logged_in_as(username):
    #            return
    #        else:
    #            self.logout()
    #    self.login(username, password)






