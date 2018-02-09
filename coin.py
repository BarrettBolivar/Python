import random

total_heads = 0
total_tails = 0
count = 0


while count < 5000:

    coin = random.randint(1, 2)

    if coin == 1:
        print("Heads!\n")
        total_heads += 1
        count += 1
        print "Attempt #", count, ": Throwing a coin... It's a head! ... Got ", total_heads, " head(s) so far and ", total_tails, " tail(s) so far"

    elif coin == 2:
        total_tails += 1
        count += 1
        print "Attempt #", count, ": Throwing a coin... It's a head! ... Got ", total_heads, " head(s) so far and ", total_tails, " tail(s) so far"
