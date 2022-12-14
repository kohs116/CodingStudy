"""
x = 3
def calc(x):
    x += 4
    return x

print(x)
print(calc(x))
print(x)
"""

"""
a = [3]

def calc(a):
    a[0] += 4
    return a

print(a)
print(calc(a))
print(a)
"""

a = [3]

def calc(a):
    a = [4]
    return a

print(a)
print(calc(a))
print(a)