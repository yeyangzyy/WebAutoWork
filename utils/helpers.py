import time
import random
import string
from datetime import datetime
import os


class Helpers:
    """工具方法类"""
    
    @staticmethod
    def generate_random_string(length: int = 8) -> str:
        """生成随机字符串"""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))
    
    @staticmethod
    def generate_random_email() -> str:
        """生成随机邮箱"""
        return f"test_{Helpers.generate_random_string(6)}@test.com"
    
    @staticmethod
    def wait(seconds: float) -> None:
        """等待指定时间"""
        time.sleep(seconds)
    
    @staticmethod
    def get_timestamp() -> str:
        """获取时间戳"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def create_directory(path: str) -> bool:
        """创建目录"""
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            print(f"创建目录失败: {e}")
            return False
    
    @staticmethod
    def highlight_element(driver, element, effect_time=0.3, color="red", border=3):
        """高亮显示元素"""
        try:
            driver.execute_script(
                f"arguments[0].style.border='{border}px solid {color}';", 
                element
            )
            time.sleep(effect_time)
            driver.execute_script(
                "arguments[0].style.border='';", 
                element
            )
        except Exception as e:
            print(f"高亮元素失败: {e}")