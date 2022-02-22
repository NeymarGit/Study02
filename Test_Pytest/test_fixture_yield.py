"""
测试yield的用法,
执行第一条测试用例时执行yield上面的代码，
执行最后一条测试用例时执行yield下面的代码
"""

import pytest


def test_one(open_brows):
    print("执行test_one")


def test_two(open_brows):
    print("执行test_two")


def test_three(open_brows):
    print("执行test_three")


if __name__ == '__main__':
    pytest.main()
