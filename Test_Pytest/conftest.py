"""
公用的fixture配置文件
"""
import pytest


@pytest.fixture() #不带参数，默认参数scope=function
def login():
    print("这是一个登录方法")


@pytest.fixture(scope="module")
def open_brows():
    print("打开浏览器")

    yield

    print("关闭浏览器")


def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签合集，用于将用例分类
    for markers in marker_list:
        config.addinivalue_line("markers", markers)
