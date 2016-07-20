import random

def coinflip():
    count = 1
    tails = 0
    heads = 0
    while count < 5001:
        random_num = round(random.random())
        if random_num == 0:
            heads = heads + 1
            print "Attempt #"+str(count) + " - It's a head. Got "+str(heads)+ "heads so far and "+str(tails)+" tails so far."
        else:
            tails = tails + 1
            print "Attempt #"+str(count) + " - It's a tail. Got "+str(heads)+ "heads so far and "+str(tails)+" tails so far."

        count = count + 1

coinflip()
