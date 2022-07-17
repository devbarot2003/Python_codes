import random



comp_guess = random.randint(1,20)
user_guess=0

def guess_number(user_guess):

    guess = 0

    while user_guess != comp_guess:
        user_guess = int(input("Guess and enter the number from 1 to 20: "))
        guess += 1
        
        print("Only enter the number between 1 to 20.") if user_guess not in range(1,21) else print("Too high!!\n") if user_guess > comp_guess else print("Too Low!!")

        
    print("\nRight Guess!!!\n")
    print(f"You took {guess} tries")


guess_number(user_guess)