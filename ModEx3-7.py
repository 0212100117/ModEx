def gcdIter(a, b):
    for i in range(a, 0, -1):
        if i == 1:
            return 1
        elif a % i == 0 and b % i == 0:
            return i


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))



