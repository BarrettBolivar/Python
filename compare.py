''' Your program should be able to accept and compare two lists: list_one and list_two. 
If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." 
Try the following test cases for lists one and two: '''
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

''' list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3] '''
counter = 0
for x in list_one:
    if list_one != list_two:
        counter = 1


if counter == 0:
    print "Same"

if counter == 1:
    print "Not the same."
