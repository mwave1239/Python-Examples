def oddevenmore(x):
    for  num in range(1,2001):
        if num % 2 == 1:
            print "The number: {} is odd.".format(num)
        else:
            print "The number: " + str(num) + " is even."

oddevenmore(1)
