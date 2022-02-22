"""
用例分组
"""

import pytest


@pytest.mark.login
def test_login1():
    print("执行登录1")


@pytest.mark.login
def test_login2():
    print("执行登录2")


@pytest.mark.search
def test_search1():
    print("执行搜索1")


@pytest.mark.search
def test_search2():
    print("执行搜索2")


if __name__ == '__main__':
    pytest.main()