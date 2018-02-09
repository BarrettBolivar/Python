#Write a program that prints a 'checkerboard' pattern to the console.
for x in range(1, 9):
    if x == 2 or x == 4 or x == 6 or x == 8:
        print "_" + "*" + "_" + "*" "_" + "*" + "_" + "*"
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 9:
        print "*" + "_" + "*" + "_" + "*" + "_" + "*" + "_"