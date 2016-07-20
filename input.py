def inputs():
    for x in range(1,11):
        y = int(raw_input("Enter your grade: "))
        if y >= 90:
            print "You got an A! \n"
        elif 90 < y >= 80:
            print "You got a B! \n"
        elif 80 < y >= 70:
            print "You got a C. \n"
        elif 70 < y >= 60:
            print "You got a D... \n"
        elif y < 60:
            print "You got an F. Dissapointed. \n"

inputs()
print "End of program. Bye!"
