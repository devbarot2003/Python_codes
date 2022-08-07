import random

computer = ["Rock", "Paper","Scissor"]

print('''WELCOME TO ROCK PAPER SCISSOR GAME\n\tEnter R for Rock\n\tEnter P for Paper\n\tEnter S for Scissor\n''')


def game():

    rounds = int(input("Enter the number of rounds: "))
    You_point,Comp_point = 0,0

    while rounds > 0:
        print("\n\nRounds Left: ", rounds)

        user_ = input("Enter your play: ")
        print()

        if user_ == "exit":
            break

        comp_ = random.choice(computer)
        
        if (user_ == "R" and comp_ == "Rock"):
            print("Your choice is: Rock\nComputer's choice is: Rock\nIt's a tie.")

        elif(user_ == "P" and comp_ == "Paper"):
            print("Your choice is: Paper\nComputer's choice is: Paper\nIt's a tie.")

        elif(user_ == "S" and comp_ == "Scissor"):
            print("Your choice is: Scissor\nComputer's choice is: Scissor\nIt's a tie.")
        
        if(user_ == "R" and comp_ == "Scissor") or (user_ == "P" and comp_ == "Rock") or (user_ == "S" and comp_ == "Paper"):
            print(f"Your choice: {user_}\nComputer's choice: {comp_}")
            print("You win Computer Lose.")
            You_point +=1
        
        elif(user_ == "S" and comp_ == "Rock") or (user_ == "R" and comp_ == "Paper") or (user_ == "P" and comp_ == "Scissor"):
            print(f"Your choice: {user_}\nComputer's choice: {comp_}")
            print("Computer win You Lose.")
            Comp_point +=1
        rounds -= 1

    if You_point>Comp_point:
        print(f"\nYou won most rounds!!\n Your points: {You_point}\nComputer points: {Comp_point}")
    elif Comp_point>You_point:
        print(f"Computer won most rounds!!\n Your points: {You_point}\nComputer points:{Comp_point}")
    else:
        print(f"Both has same points!!\n Your points: {You_point}\nComputer points:{Comp_point}")

game()