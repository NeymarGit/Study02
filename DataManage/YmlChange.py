'''
读写yaml文件
'''

import yaml


def write_yaml():
    with open("demo.yaml", "w") as f:
        datas = {'name': [[1,2],[4,3]]}
        # datas = [{'liu', 'yang', 'he'},{'1', '2', '3'}]
        yaml.dump(data=datas, stream=f)


def read_yaml():
    result = yaml.load(open("demo.yaml"), Loader=yaml.FullLoader)
    print(result)


if __name__ == '__main__':
    # read_yaml()
    write_yaml()
