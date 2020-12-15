from selenium import webdriver


class LoginPage():
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_css = '[value="Log in"]'
    link_logout_linktext = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        username_box = self.driver.find_element_by_id(self.textbox_username_id)
        username_box.clear()
        username_box.send_keys(username)

    def set_password(self, password):
        password_box = self.driver.find_element_by_id(self.textbox_password_id)
        password_box.clear()
        password_box.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element_by_css_selector(self.button_login_css)
        login_button.click()

    def click_logout_button(self):
        logout_button = self.driver.find_element_by_link_text(self.link_logout_linktext)
        logout_button.click()
