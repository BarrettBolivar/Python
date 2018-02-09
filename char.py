''' Write a program that takes a list of strings and a string containing a single character, 
and prints a new list of all the strings containing that character. '''
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newStr =""
for i in word_list:
    for x in char:
        if char in i:
            newStr += i

print newStr
''' 
for item in wordlist:
    for character in letters:
        if character in item:
            print item
            break '''