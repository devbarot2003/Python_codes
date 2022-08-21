import random

lst = ["s","w","g"]

def game(rounds):

    comp_point=0
    user_point=0

    print("\n\tWELCOME TO SNAKE, WATER, GUN GAME:\n\t     \"s\" for SNAKE\n\t     \"g\" for GUN\n\t     \"w\" for WATER")

    while (rounds != 0):

        rounds -= 1
        user = input("\nEnter your play: ")
        comp = random.choice(lst)
        print(f"Computer's play: {comp}")

        if (comp == "s" and user == "s") or (comp == "g" and user == "g") or (comp == "w" and user == "w"):
            print("Both played the same move, it's a tie.")

        if (comp == "s" and user == "w") or (comp == "g" and user == "s") or (comp == "w" and user == "g"):
            print("Computer wins the play, 1 point alloted to computer!!")
            comp_point += 1

        if (comp == "w" and user == "s") or (comp == "s" and user == "g") or (comp == "g" and user == "w"):
            print("User wins the play, 1 point alloted to user!!")
            user_point += 1
        print(f"\n\tRounds left: {rounds}\n")

    print(f"Total point of user: {user_point}")
    print(f"Total point of computer: {comp_point}")

    if user_point>comp_point:
        print("\n-----USer wins the most rounds. Congratulations!!-----")

    elif comp_point>user_point:
        print("\n-----Computer wins the most rounds. Better luck next time!!-----")
    
    elif comp_point == user_point:
        print("\n-----Both of you played very hard game. It's a tie!!-----")

rounds = int(input("Enter the number of rounds you want to play: "))

game(rounds)