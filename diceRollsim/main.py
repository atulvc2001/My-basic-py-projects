import random
import time

while True:
    print("1.Roll the Dice       2.exit")
    time.sleep(1)
    userinp = int(input("What would you like to do?\n "))
    time.sleep(1)
    if userinp == 1:
        number = random.randint(1,6)
        print("the number is: %d" % (number))
        time.sleep(3)

    else:
        print("you have exited")
        break


