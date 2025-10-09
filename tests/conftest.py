import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from utils.driver_manager import DriverManager
from config.config import Config
import logging


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """初始化浏览器驱动"""
    driver_manager = DriverManager()
    driver = driver_manager.create_driver()
    
    # 设置基础URL
    driver.get(Config.BASE_URL)
    
    yield driver
    
    # 测试结束后关闭浏览器
    driver.quit()


@pytest.fixture(scope="function")
def logger():
    """日志记录器"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)