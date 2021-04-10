from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page))

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)

    #Methods for lifesum Signup
    def verify_title_exists(self, title_text):
        #Verify goal text exists
        assert title_text in self.driver.find_element_by_id("Welcome_Bar").text, \
            "Button not found".format(title_text)

    def tear_down(self):
        #Quit the browser
        self.driver.quit()


webapp = WebApp.get_instance()
