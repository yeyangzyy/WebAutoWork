import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TestExample:
    """示例测试类"""
    
    def test_baidu_search(self, driver: WebDriver):
        """百度搜索测试示例"""
        base_page = BasePage(driver)
        
        # 定位器
        SEARCH_INPUT = (By.ID, "chat-textarea")
        SEARCH_BUTTON = (By.ID, "chat-submit-button")
        
        # 执行搜索操作
        assert base_page.input_text(SEARCH_INPUT, "自动化测试"), "搜索框输入失败"
        assert base_page.click(SEARCH_BUTTON), "搜索按钮点击失败"
        
        # 验证搜索结果
        assert base_page.is_element_visible((By.ID, "content_left")), "搜索结果未显示"
    
    def test_page_title(self, driver: WebDriver):
        """页面标题测试示例"""
        base_page = BasePage(driver)
        
        # 验证页面标题
        expected_title = "百度一下，你就知道"
        actual_title = driver.title
        
        assert actual_title == expected_title, f"页面标题不匹配，期望: {expected_title}, 实际: {actual_title}"