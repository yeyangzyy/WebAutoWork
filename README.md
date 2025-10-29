# 接口自动化测试项目

基于Python + pytest + requests + selenium的web自动化测试框架。

## 项目结构
WebAutoWork
├── 📁 config/                 # 配置文件
│   ├── __init__.py
│   ├── dev.env               # 开发环境配置
│   ├── prod.env              # 生产环境配置
│   └── config.py             # 配置读取逻辑
├── 📁 pages/                  # 页面基础封装类方法
│   ├── base_page.py        # 页面基类，封装常用操作方法
├── 📁 reports/               # 测试报告输出目录
│   └── .gitkeep
├── 📁 tests/             # 测试用例
│   ├── __init__.py
│   └── test_example.py   # 测试实例
├── 📁 utils/             # 工具类
│   ├── __init__.py
│   └──helpers.py          # 工具方法类
├── 📄 requirements.txt       # 项目依赖列表(pip)
├── 📄 environment.yml       # 项目环境列表(conda)
├── 📄 .gitignore            # Git忽略配置
└── 📄 README.md             # 项目说明文档
## 环境要求

- Python 3.8+
- pip

## 安装依赖

```bash
# conda 的用法
conda env create -f environment.yml

pip install -r requirements.txt

# 使用pytest运行测试
pytest test_example.py



