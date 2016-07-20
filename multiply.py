def multiply(a, num):
    b = [num * x for x in a]

a = [2,4,10,16]
num = 5
b = []
b = multiply(a, num)
b = [5 * x for x in a]
print b
