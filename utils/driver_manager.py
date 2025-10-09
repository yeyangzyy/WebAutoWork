from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import Config
import logging


class DriverManager:
    """浏览器驱动管理类"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = Config.get_browser_config()
    
    def create_driver(self) -> webdriver.Remote:
        """创建浏览器驱动实例"""
        browser = self.config["browser"].lower()
        
        if browser == "chrome":
            return self._create_chrome_driver()
        elif browser == "firefox":
            return self._create_firefox_driver()
        elif browser == "edge":
            return self._create_edge_driver()
        else:
            raise ValueError(f"不支持的浏览器: {browser}")
    
    def _create_chrome_driver(self) -> webdriver.Chrome:
        """创建Chrome驱动"""
        options = webdriver.ChromeOptions()
        
        if self.config["headless"]:
            options.add_argument("--headless")
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={self.config['window_size'][0]},{self.config['window_size'][1]}")
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        self._set_driver_properties(driver)
        self.logger.info("Chrome浏览器驱动创建成功")
        return driver
    
    def _create_firefox_driver(self) -> webdriver.Firefox:
        """创建Firefox驱动"""
        options = webdriver.FirefoxOptions()
        
        if self.config["headless"]:
            options.add_argument("--headless")
        
        options.add_argument(f"--width={self.config['window_size'][0]}")
        options.add_argument(f"--height={self.config['window_size'][1]}")
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        
        self._set_driver_properties(driver)
        self.logger.info("Firefox浏览器驱动创建成功")
        return driver
    
    def _create_edge_driver(self) -> webdriver.Edge:
        """创建Edge驱动"""
        options = webdriver.EdgeOptions()
        
        if self.config["headless"]:
            options.add_argument("--headless")
        
        options.add_argument(f"--window-size={self.config['window_size'][0]},{self.config['window_size'][1]}")
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        
        self._set_driver_properties(driver)
        self.logger.info("Edge浏览器驱动创建成功")
        return driver
    
    def _set_driver_properties(self, driver: webdriver.Remote) -> None:
        """设置驱动属性"""
        driver.implicitly_wait(self.config["implicit_wait"])
        driver.set_page_load_timeout(self.config["page_load_timeout"])
        if not self.config["headless"]:
            driver.maximize_window()