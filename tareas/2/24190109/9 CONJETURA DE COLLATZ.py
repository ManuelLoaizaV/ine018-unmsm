a = int(input())

while a > 1:
    if a % 2 == 0:
        a //= 2
    else:
        a = 3 * a + 1
    print(a)
