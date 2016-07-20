def sum(a):
    i = 0
    temp = 0
    for i in range(0, len(a)):
        temp += a[i]
    print "The values of the list add up to: " + str(temp)
a = [1, 2, 5, 10, 255, 3]
sum(a)
