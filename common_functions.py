def judge_palindrome(num):
    # 判断回文数
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False


def factoring(num):
    # 因式分解
    arr = []
    i = 2
    while num != 1:
        if num % i == 0:
            while num % i == 0:
                arr.append(i)
                num /= i
        i += 1
    return arr


def prime_num(num):
    if num in [0, 1]:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
