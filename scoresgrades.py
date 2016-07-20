def scores():
    print "Scores and Grades"
    count = 0
    while count < 11:
        testscore = input("Score: ")
        if testscore > 100:
            print "; Your test score is invalid. \n"
        elif testscore >= 90:
            print "; You got an A! \n"
        elif testscore >= 80:
            print "; You got a B! \n"
        elif testscore >= 70:
            print "; You got a C. \n"
        elif testscore >= 60:
            print "; You got a D. Come on. \n"
        elif testscore < 60:
            print "; try again. You got an F."
        count += 1

scores()
