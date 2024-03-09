"""def F(A):
    for x in range(1000):
        for y in range(1000):
            if not ((x + 2 * y < A) or (y > x) or (x > 60)):
                return False
    return True



for A in range(1000):
    if F(A):
        print(A)
        break
"""
def F(A, B):
    for x in range(1000):
        if not (not(x <= 50 and x >= 20) or (x <= B and x >= A)) and (not (x <= B and x >= A) or (x >= 10 and x <= 60)):
            return False
    return True



for i in range(100):
    for y in range(i, 100):
        if F(i, y):
            print(y - i, i, y)

