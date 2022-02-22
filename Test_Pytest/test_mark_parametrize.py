"""
pytest方法的参数化
"""
import pytest
import yaml


# 1、直接传参数
@pytest.mark.skip  # 跳过执行
@pytest.mark.parametrize(["actual", "expect"], [("3+2", 5), ("1+5", 13), ("2*2", 4)])
def test_parame(actual, expect):
    assert eval(actual) == expect


# 2、参数组合
@pytest.mark.skip
@pytest.mark.parametrize("x", [4, 5])
@pytest.mark.parametrize("y", [6, 7, 8])
def test_comb(x, y):
    print("测试数据组合x:{0},y:{1}", (x, y))


# 3、将方法传递到参数中
test_user_data = ["Neymar", "Messi"]


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print("登录的用户为：", user)
    return user


#  indirect=True是优先把参数当做函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    name = login_r
    print("login的返回值为：", name)


# 4、直接读取yaml文件
@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
def test_yaml_data(a, b):
    print(a + b)


if __name__ == '__main__':
    pytest.main()
