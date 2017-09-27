import random

def rock_paper_scissors_game():
	user_turn = raw_input("Choose: rock, paper or scissors.")
	computer_choice = ["rock", "paper", "scissors"]
	computers_turn = random.choice(computer_choice)
	user_pick = user_turn.lower()
	print("You have selected " + user_pick)
	print("Your opponent selected " + computers_turn)
	if user_pick == computers_turn:
		print("It's a draw. Play again.")
	elif user_pick == "rock" and computers_turn == "paper":
		print("Paper covers rock, you lose.")
	elif user_pick == "rock" and computers_turn == "scissors":
		print("Rock breaks scissors, you win!")
	elif user_pick == "paper" and computers_turn == "rock":
		print("Paper covers rock, you win.")
	elif user_pick == "paper" and computers_turn == "scissors":
		print("Scissors cuts paper, you lose.")
	elif user_pick == "scissors" and computers_turn == "rock":
		print("Rock breaks scissors, you lose!")
	elif user_pick == "scissors" and computers_turn == "paper":
		print("Scissors cuts paper, you win.")
	else:
		print("Nice choice")


