def isDiffOne(n):
    prev = -1
    while n > 0:
        cur = n % 10
        if prev != -1:
            if (abs(cur - prev) != 1):
                return False
        n = n // 10
        prev = cur
    return True

input = int(input("Input: "))
print("Output:")
for i in range(input):
    if (isDiffOne(i)):
        print(i, end=", ")