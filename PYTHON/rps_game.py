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
        
        print("Your choice is: Rock\nComputer's choice is: Rock\nIt's a tie.") if (user_ == "R" and comp_ == "Rock") else print("Your choice is: Paper\nComputer's choice is: Paper\nIt's a tie.") if(user_ == "P" and comp_ == "Paper") else print("Your choice is: Scissor\nComputer's choice is: Scissor\nIt's a tie.") if(user_ == "S" and comp_ == "Scissor") else print()
            
        print(f"Your choice: {user_}\nComputer's choice: {comp_}"); print("You win Computer Lose."); You_point +=1 if(user_ == "R" and comp_ == "Scissor") or (user_ == "P" and comp_ == "Rock") or (user_ == "S" and comp_ == "Paper") else print(f"Your choice: {user_}\nComputer's choice: {comp_}"); print("Computer win You Lose.");Comp_point +=1 if (user_ == "S" and comp_ == "Rock") or (user_ == "R" and comp_ == "Paper") or (user_ == "P" and comp_ == "Scissor") else print()
        
        rounds -= 1
    print(f"\nYou won most rounds!!\n Your points: {You_point}\nComputer points: {Comp_point}") if You_point>Comp_point else print(f"Computer won most rounds!!\n Your points: {You_point}\nComputer points:{Comp_point}") if Comp_point>You_point else print(f"Both has same points!!\n Your points: {You_point}\nComputer points:{Comp_point}")

game()