''' Create a function called odd_even that counts from 1 to 2000. 
As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number. '''
''' def odd_even():
    for x in range(1, 2000):
        if x % 2 == 0:
            print x, "even"
        if x % 2 != 0:
            print x, "odd"
odd_even() '''

''' Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
and returns a list where each value has been multiplied by 5. '''

def multiply(list1, a):
    for i in list1:
        x = i * a
        loc = list1.index(i)
        list1.remove(i)
        list1.insert(loc, x)
    return list1


''' Write a function that takes the multiply function call as an argument. Your new function should return 
the multiplied list as a two-dimensional list. 
Each internal list should contain the 1's times the number in the original list. Here's an example: '''
def layered_multiples(arr):
    new_array = []
    new_array1 = []
    for index in arr:
        count = 0
        new_array1 = []
        while index > count:
            new_array1.insert(count, 1)
            count += 1
        new_array.append(new_array1)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
