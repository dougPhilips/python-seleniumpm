from selenium import webdriver

class UiTestWrapper(object):
    driver = None

    @classmethod
    def setup_class(self):
        # server = 'http://localhost:4444/wd/hub'
        # capabilities = webdriver.DesiredCapabilities.PHANTOMJS
        # capabilities = webdriver.DesiredCapabilities.FIREFOX
        # self.driver = webdriver.Remote(command_executor=server, desired_capabilities=capabilities)
        # self.driver = webdriver.Firefox(capabilities=webdriver.DesiredCapabilities.FIREFOX)
        self.driver = webdriver.PhantomJS()

    @classmethod
    def teardown_class(self):
        if self.driver:
            self.driver.quit()
