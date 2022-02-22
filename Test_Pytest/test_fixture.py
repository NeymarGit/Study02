"""
测试fixture
"""

import pytest


# 参数传入一个方法，执行test_one前先执行login方法
def test_one(login):
    print("test_one需要登录")


def test_two():
    print("test_two不需要登录")


def test_three(login):
    print("test_three需要登录")


if __name__ == '__main__':
    pytest.main()
