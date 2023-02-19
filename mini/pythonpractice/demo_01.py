from itertools import combinations

x = ["a", "b", "c", "d", "e", "f", "g"]
num = 2

def com(x, n=2):
    result = []
    if n < 2:
        return x
    else:
        for i in range(n-1, len(x)):
            record = ["*".join([item, x[i]]) for item in com(x[0:i], n-1)]
            result.extend(record)
        return result

print(com(x, num))
result1 = sorted(com(x, num))
result2 = sorted(["*".join(item) for item in combinations(x, num)])
print(result1)
print(result1 == result2)

for n in range(2, 6):
    result1 = sorted(com(x, n))
    result2 = sorted(["*".join(item) for item in combinations(x, n)])
    print(n, result1 == result2)