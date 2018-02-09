''' Your program input will always be a list. For each item in the list, test its data type. 
If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. 
At the end of your program print the string, the number and an analysis of what the list contains. 
If it contains only one type, print that type, otherwise, print 'mixed'. '''
#l = ['magical unicorns',19,'hello',98.98,'world']
l = [2,3,1,7,4,12]
newliststr = ""
newlistint = 0
countStr = 0
countInt = 0
for x in range(len(l)):
    if isinstance(l[x], str):
        countStr += 1
        newliststr += l[x]
    if isinstance(l[x], (int, float)):
        countInt += 1
        newlistint += l[x]

if countInt == len(l):
    print "This list only has numbers"
    print newlistint
if countStr == len(l):
    print "This list only has"
    print newliststr
if countInt != len(l) and countStr != len(l):
    print "This is a mixed list."
    print newlistint
    print newliststr