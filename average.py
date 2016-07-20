def average(a):
    i = 0
    temp = 0
    for i in range(0, len(a)):
        temp += a[i]
    temp1 = temp/len(a)
    print "The average of the listis: " + str(temp1)
a = [1, 2, 5, 10, 255, 3]
average(a)
