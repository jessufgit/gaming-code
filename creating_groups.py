# First I need to import some functionality from the random library that will help me select players and teams randomly

from random import randint
from random import choice

#I created two empty lists to store the players who are being selected, a list containing the two groups they could be assigned to,
# and a list of players.

teamOne = []
teamTwo = []
allTeams = [teamOne, teamTwo]
players = ["Jessica", "Avery", "Brennan", "Jay", "Karen", "Chris", "CJ", "Clay", "Max"]

# I created a list that held the two group names to which teams could be assigned. I also assigned a
# variable to hold the total number of players.

group_names = ["Gators", "Seminoles"]
number_of_players = 9

#This code tells the reader what is going to happen - x # of players will be assigned randomly to two teams: Gators and Seminoles.
print("There are " + str(number_of_players) + " players that need to be split between two teams: the " +
	group_names[0] + " and the " + group_names[1] + ".")
print("\n")
print("I will now randomly assign each player to a different team.")
print("\n")

# The while statement runs as long as there are players left to place.
# Each time a player is randomly assigned to a team, the number of players left to assign decreases by one.
# If the number of players on the randomly selected team is less than 5, it will append the list to include the player that was randomly
#selected. If the number of players on the randomly selected team is greater than 5, it will default to assigning them to the other team.
# Print messages tell which player is assigned to what team and how many players are left to assign.
while number_of_players > 0:
	selectedPlayer = choice(players)
	selectedTeam = choice(group_names)
	print(selectedPlayer + " was selected to be on....")
	print("the " + selectedTeam)

	if selectedTeam == "Gators" and len(teamOne) <= 4:
		if len(teamOne) == 0:
			teamOne.append(selectedPlayer)
			players.remove(selectedPlayer)
			number_of_players -= 1
			print(str(number_of_players) + " players still need to be placed on a team.")
			print(str(len(teamOne)) + " player is now on the Gators.")
			print("\n")
		else:
			teamOne.append(selectedPlayer)
			players.remove(selectedPlayer)
			number_of_players -= 1
			print(str(number_of_players) + " players still need to be placed on a team.")
			print(str(len(teamOne)) + " players are on the Gators.")
			print("\n")
	elif selectedTeam == "Seminoles" and len(teamTwo) <= 4:
		if len(teamTwo) == 0:
			teamTwo.append(selectedPlayer)
			players.remove(selectedPlayer)
			number_of_players -= 1
			print(str(number_of_players) + " players still need to be placed on a team.")
			print(str(len(teamTwo)) + " player is now on the Seminoles.")
			print("\n")
		else:
			teamTwo.append(selectedPlayer)
			players.remove(selectedPlayer)
			number_of_players -= 1
			print(str(number_of_players) + " players still need to be placed on a team.")
			print(str(len(teamTwo)) + " players are on the Seminoles.")
			print("\n")
	elif selectedTeam == "Gators" and len(teamOne) > 4:
		print("Sorry, that team is full, so " + selectedPlayer + " will be placed on the Seminoles.")
		teamTwo.append(selectedPlayer)
		players.remove(selectedPlayer)
		number_of_players -= 1
		group_names.remove(selectedTeam)
	elif selectedTeam == "Seminoles" and len(teamTwo) > 4:
		print("Sorry, that team is full, so " + selectedPlayer + " will be placed on the Gators.")
		teamOne.append(selectedPlayer)
		players.remove(selectedPlayer)
		number_of_players -= 1
		group_names.remove(selectedTeam)
	else:
		print(len(players))
		print(len(teamTwo))


# This final code prints the assignments by team.
print("The final lineup for the Gators:" + str(teamOne))
print("The final lineup for the Seminoles:" + str(teamTwo))
