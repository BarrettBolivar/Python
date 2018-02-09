''' Create a function that takes in two lists and creates a single dictionary.
 The first list contains keys and the second list contains the values. Assume the lists will be of equal length. '''
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(list1, list2):
    temp = []
    if len(list1) < len(list2):
        temp = list1
        list1 = list2
        list2 = temp
    new_dict = {}
    new_dict = zip(list1, list2)
    return new_dict

print make_dict(name, favorite_animal)