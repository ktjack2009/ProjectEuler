from common_functions import *
from functools import reduce


def answer_1(num=1000):
    # 计算小于1000的自然数中是3或者5的倍数的所有数的和
    result = sum([i for i in range(1, num) if i % 3 == 0 or i % 5 == 0])
    return result


def answer_2(num=4000000):
    # 计算最后一项不超过400万的斐波拉契数列中所有偶数之和
    a, b = 1, 1
    result = 0
    while a + b <= num:
        a, b = b, a + b
        if b % 2 == 0:
            result += b
    return result


def answer_3(num=60051475143):
    # 13195的素因数为5， 17， 13，和29。求60051475143的最大素因数
    arr = []
    i = 2
    while num != 1:
        if num % i == 0:
            # 如果能被分解
            while num % i == 0:
                arr.append(i)
                num /= i
        i += 1
    return max(arr)


def answer_4():
    # 由两个2位数相乘得到的最大乘积回文数是 9009 = 91 * 99
    # 找出由两个3位数相乘得到的最大乘积回文数
    result = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            _ = i * j
            if judge_palindrome(_) and (_ > result):
                result = _
    return result


def answer_5():
    # 能被1到10这10个整数整除的最小正数是2520，计算最小的能够被1到20整除的正数
    arr = []
    num_arr = sorted(list(range(2, 21)), reverse=True)
    for num in num_arr:
        _ = factoring(num)  # 因式分解后的结果
        for i in _:
            while _.count(i) > arr.count(i):
                arr.append(i)
    return reduce(lambda x, y: x * y, arr)
