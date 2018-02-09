words = "It's thanksgiving day. It's my birthday,too!"
#print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
x = words.find('day')
print x
y = words.replace('day', 'month')
print words

q = [2,54,-2,7,12,98]
print min(q)
print max(q)

w = ["hello",2,54,-2,7,12,98,"world"]
print w[0]
wLength = len(w) - 1
print w[wLength]

e = [19,2,54,-2,7,12,98,32,10,-3,6]
e.sort()
eLength = len(e) - 1
eLenghtHalf = eLength / 2
frontHalf = e[:eLenghtHalf]
e = e[eLenghtHalf:]
e.insert(0, frontHalf)
print e
