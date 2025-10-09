from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
from typing import Tuple, Optional


class BasePage:
    """页面基类，封装常用操作方法"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)
    
    def open(self, url: str) -> None:
        """打开指定URL"""
        self.driver.get(url)
        self.logger.info(f"打开页面: {url}")
    
    def find_element(self, locator: Tuple[By, str], timeout: int = 10) -> Optional[WebDriver]:
        """查找单个元素"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"元素查找超时: {locator}")
            return None
    
    def find_elements(self, locator: Tuple[By, str], timeout: int = 10) -> list:
        """查找多个元素"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"元素组查找超时: {locator}")
            return []
    
    def click(self, locator: Tuple[By, str], timeout: int = 10) -> bool:
        """点击元素"""
        element = self.find_element(locator, timeout)
        if element:
            try:
                element.click()
                self.logger.info(f"点击元素: {locator}")
                return True
            except Exception as e:
                self.logger.error(f"点击元素失败: {locator}, 错误: {e}")
                return False
        return False
    
    def input_text(self, locator: Tuple[By, str], text: str, timeout: int = 10) -> bool:
        """输入文本"""
        element = self.find_element(locator, timeout)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                self.logger.info(f"在元素 {locator} 输入文本: {text}")
                return True
            except Exception as e:
                self.logger.error(f"输入文本失败: {locator}, 错误: {e}")
                return False
        return False
    
    def get_text(self, locator: Tuple[By, str], timeout: int = 10) -> Optional[str]:
        """获取元素文本"""
        element = self.find_element(locator, timeout)
        if element:
            try:
                text = element.text
                self.logger.info(f"获取元素文本: {locator} -> {text}")
                return text
            except Exception as e:
                self.logger.error(f"获取文本失败: {locator}, 错误: {e}")
                return None
        return None
    
    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 5) -> bool:
        """检查元素是否可见"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"元素可见: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"元素不可见: {locator}")
            return False
    
    def wait_for_element_clickable(self, locator: Tuple[By, str], timeout: int = 10) -> bool:
        """等待元素可点击"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable(locator))
            self.logger.info(f"元素可点击: {locator}")
            return True
        except TimeoutException:
            self.logger.error(f"元素不可点击: {locator}")
            return False
    
    def take_screenshot(self, filename: str) -> bool:
        """截取屏幕截图"""
        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"截图保存: {filename}")
            return True
        except Exception as e:
            self.logger.error(f"截图失败: {e}")
            return False
    
    def switch_to_frame(self, locator: Tuple[By, str]) -> bool:
        """切换到iframe"""
        try:
            frame = self.find_element(locator)
            if frame:
                self.driver.switch_to.frame(frame)
                self.logger.info(f"切换到iframe: {locator}")
                return True
        except Exception as e:
            self.logger.error(f"切换iframe失败: {e}")
        return False
    
    def switch_to_default_content(self) -> None:
        """切换回默认内容"""
        self.driver.switch_to.default_content()
        self.logger.info("切换回默认内容")