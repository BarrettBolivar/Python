#Create a function called draw_stars() that takes a list of numbers and prints out *.

def draw_stars(arr):
    for i in range(len(arr)):
        count = 0
        if type(arr[i]) == int:
            while arr[i] > count:
                print "*",
                count +=1
            print ""

        if type(arr[i]) == str:
            x = len(arr[i])
            y = arr[i]
            first_letter = y[0]
            while x > count:
                print first_letter ,
                count += 1

draw_stars([2,4, "Jason"])

''' Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function.
 When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
You may use the .lower() string method for this part. '''
