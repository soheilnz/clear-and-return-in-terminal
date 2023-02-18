import time

CLEAR = "\033[2J" #this line!
CLEAR_AND_RETURN = "\033[H" #this line!

number = 10
print(CLEAR) #this line!
while number != 30:
    print(f"{CLEAR_AND_RETURN} {number}") # this line!
    time.sleep(1)
    number += 1