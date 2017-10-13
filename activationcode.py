import random
import string


def gene_code(number, length):
    '''

    :param number: 激活码个数
    :param length: 激活码长度
    :return:
    '''

    result = []
    source = list(string.ascii_uppercase)  #添加26个英文字母   --可追加小写

    for index in range(0, 10):   #添加阿拉伯数字
        source.append(str(index))

    while len(result) < number:
        key = ''
        for index in range(length):
            key += random.choice(source)
        if key in result:
            pass
        else:
            result.append(key)

    for key in result:
        print(key)


if __name__ == '__main__':
    number = 10
    length = 18
    gene_code(number, length)




