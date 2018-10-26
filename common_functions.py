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
