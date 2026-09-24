def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num