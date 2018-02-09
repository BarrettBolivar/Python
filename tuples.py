my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tu():
    my_tuple = ()
    my_dict1 =[]
    temp_dict =[]
    for key, data in my_dict.items():
        temp_dict += key,
        temp_dict += data,
        z = tuple(temp_dict)
        my_tuple = my_tuple + z
        temp_dict.remove(key)
        temp_dict.remove(data)
    my_dict1.append(my_tuple)
    print my_dict1
tu()


''' 
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")] '''