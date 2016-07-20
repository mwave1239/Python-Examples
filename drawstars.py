#def drawstars(x):
#    for num in x:
#        print "*"*num

def drawstars2(x):
    for num in x:
        if type(num) == str:
            tempval = num.lower()
            tempval1 = tempval[0]
            itterate=0
            for i in xrange(0, len(num)):
                itterate = itterate + 1
            print tempval1*itterate
        else:
            print "*"*num

#x = [4, 6, 1, 3, 5, 7, 25]
#drawstars(x)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawstars2(x)
