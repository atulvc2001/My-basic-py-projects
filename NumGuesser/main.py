import random 
import time

print("Welcome to the NumGuesser!")

def main():
    time.sleep(1)
    rando = random.randint(1,10)
    time.sleep(0.5)
    for i in range(0,3):
        num = int(input("Enter a number between 1 to 10\n "))
        turn = 3-i
        if num == rando :
            print( f"*** congrats, you have guessed the number {num} correctly! ***")
            exit()
        elif num != rando :
            print(f"wrong guess")
            print("\nBetter luck next time!\n")
            print(f"you have {turn - 1} turns left")
            continue
        else:
            break
    print(f"the correct number was {rando}")

if __name__ == "__main__":
    while True:
        main()
        ans = str(input("do you want to continue or exit?\n Press Y to continue or press N to exit: ")).lower()
        if ans == 'y':
            main()
        else:
            print("Have a good day!")
            exit()
            
            
        





