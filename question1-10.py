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


def answer_5(num=20):
    # 能被1到10这10个整数整除的最小正数是2520，计算最小的能够被1到20整除的正数
    arr = []
    num_arr = sorted(list(range(2, num + 1)), reverse=True)
    for num in num_arr:
        _ = factoring(num)  # 因式分解后的结果
        for i in _:
            while _.count(i) > arr.count(i):
                arr.append(i)
    return reduce(lambda x, y: x * y, arr)


def answer_6(num=100):
    # 求前100个自然数平方的和与和的平方之差
    sum1 = sum([i ** 2 for i in range(1, num + 1)])
    sum2 = sum([i for i in range(1, num + 1)]) ** 2
    return sum2 - sum1


def answer_7():
    # 求第10001个素数
    i = 2
    d = 1
    while d != 10001:
        i += 1
        if prime_num(i):
            d += 1
    return i


def answer_8():
    # 在1000个正整数中，找到连续4个数，使其乘积最大
    a = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    result = 0
    index = 0
    for i in range(len(a) - 3):
        base = [int(j) for j in a[i: i + 4]]
        if reduce(lambda x, y: x * y, base) >= result:
            result = max(reduce(lambda x, y: x * y, base), result)
            index = i
    return list(a[index:index + 4]), result


def answer_9():
    # 有且只有一个毕达哥拉斯三元组满足a+b+c=1000, a<b<c, a**2+b**2=c**2。求这个三元组的乘积abc。
    for c in range(334, 998):
        for b in range(int(c / 2) + 1, c):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c, a * b * c


def answer_10_1():
    # 求小于两百万的所有素数之和
    result = 0
    for i in range(2000000):
        if prime_num(i):
            result += i
    return result


def answer_10_2(num):
    # 消去合数，只循环一次
    an = [True] * num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if an[i]:
            an[i * i::2 * i] = [False] * int((num - i * i - 1) / (2 * i) + 1)
    prime_list = [2] + [j for j in range(3, num, 2) if an[j]]
    return sum(prime_list)
