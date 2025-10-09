
### 3. config/config.py
import os
from typing import Dict, Any


class Config:
    """配置管理类"""
    
    # 浏览器配置
    BROWSER = "chrome"  # chrome, firefox, edge
    HEADLESS = False
    WINDOW_SIZE = (1920, 1080)
    IMPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # 测试环境配置
    BASE_URL = "https://www.baidu.com"
    
    # 测试数据配置
    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "test_data")
    
    # 报告配置
    REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "reports")
    
    @classmethod
    def get_browser_config(cls) -> Dict[str, Any]:
        """获取浏览器配置"""
        return {
            "browser": cls.BROWSER,
            "headless": cls.HEADLESS,
            "window_size": cls.WINDOW_SIZE,
            "implicit_wait": cls.IMPLICIT_WAIT,
            "page_load_timeout": cls.PAGE_LOAD_TIMEOUT
        }