from datetime import datetime

print("\n\t\tWelcome to Dev's Health Management System.")

def getTime():
    return datetime.now()

while True:
    print("\nHere are your 3 clients:\n\n1.Devkumar\n2.Devasya\n3.Manthan")

    client = int(input("\nChoose your Client:\nEnter 1 for \"Devkumar\"\nEnter 2 for \"Devasya\"\nEnter 3 for \"Manthan\"\nEnter 4 for \"Ishit\"\nEnter 5 for \"Exit\" the system\nYour Answer: "))
    
    if client == 1:
        work = int(input("Enter 1 for \"Exercise\" and 2 for \"Food\""))

        decision = int(input("\nEnter 1 to Add the data of client.\nEnter 2 to retrieve the data of client\nYour Answer: "))
        if work == 1:
            if decision == 1:
                inp = input("Enter the data: ")
                with open("dev_exercise.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")
            elif decision == 2:
                with open("dev_exercise.txt") as f:
                    print(f.read())

    if client == 1:
        work = int(input("Enter 1 for \"Exercise\" and 2 for \"Food\""))

        decision = int(input("\nEnter 1 to Add the data of client.\nEnter 2 to retrieve the data of client\nYour Answer: "))
        if work == 1:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("dev_exercise.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:

                with open("dev_exercise.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")

        elif work == 2:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("dev_food.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:

                with open("dev_food.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")
        else:
            print("\n*Please enter valid value*\n")
    
    elif client == 2:

        work = int(input("Enter 1 for \"Exercise\" and 2 for \"Food\""))
        decision = int(input("\nEnter 1 to Add the data of client.\nEnter 2 to retrieve the data of client\nYour Answer: "))

        if work == 1:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("devasya_exercise.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:

                with open("devasya_exercise.txt") as f:
                    print(f.read())

        elif work == 2:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("devasya_food.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:

                with open("devasya_food.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")
        else:
            print("\n*Please enter valid value*\n")
    
    elif client == 3:

        work = int(input("Enter 1 for \"Exercise\" and 2 for \"Food\""))
        decision = int(input("\nEnter 1 to Add the data of client.\nEnter 2 to retrieve the data of client\nYour Answer: "))

        if work == 1:

            if decision == 1:
                inp = input("Enter the data: ")
                with open("manthan_exercise.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:
                with open("manthan_exercise.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")
        
        elif work == 2:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("manthan_food.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:
                with open("manthan_food.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")

    elif client == 4:

        work = int(input("Enter 1 for \"Exercise\" and 2 for \"Food\""))
        decision = int(input("\nEnter 1 to Add the data of client.\nEnter 2 to retrieve the data of client\nYour Answer: "))

        if work == 1:

            if decision == 1:
                inp = input("Enter the data: ")
                with open("ishit_exercise.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:
                with open("ishit_exercise.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")
        
        elif work == 2:

            if decision == 1:

                inp = input("Enter the data: ")
                with open("ishit_food.txt","a") as f:
                    f.write(str([str(getTime())])+": "+inp+"\n")

            elif decision == 2:
                with open("ishit_food.txt") as f:
                    print(f.read())

            else:
                print("\n*Please enter valid value*\n")
    elif client == 5:
        print("\n\t\tThank you for visiting my system 😀\n")
        break