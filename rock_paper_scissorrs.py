computer_choice = 'scissors'
user_choice = input("Do you want to rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("TIE!!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("YOU WIN!")
elif user_choice == "paper" and computer_choice == "rock":
    print("YOU WIN!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("YOU WIN!")
else:
    print("you lose :( , the computer WINS!! :)")