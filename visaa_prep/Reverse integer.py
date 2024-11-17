def reverse_integer(n):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1]) * sign
    if INT_MIN <= reversed_num <= INT_MAX:
        return reversed_num
    else:
        return 0
n = int(input().strip())
print(reverse_integer(n))
