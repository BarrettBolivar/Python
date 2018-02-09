''' Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this: '''
#Use the python random module to generate a random number
def grade_it(numgra):
    print numgra
    if numgra > 60 and numgra < 69:
        print "Score: 60 - 69; Grade - D"

    if numgra > 70 and numgra < 79:
        print "Score: 70 - 79; Grade - C"

    if numgra > 80 and numgra < 89:
        print "Score: 80 - 89; Grade - B"

    if numgra > 90 and numgra < 100:
        print "Score: 90 - 100; Grade - A"

import random
random_num = random.random() * 100
grade_it(random_num)