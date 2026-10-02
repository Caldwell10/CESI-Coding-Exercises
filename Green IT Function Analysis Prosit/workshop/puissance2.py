
def puissance2(p, n):
    if n == 0:
        return 1
    half = puissance2(p, n //2)
    if n % 2 == 0:
        return half * half  # one operation
    else:
        return half * half * p # two operations