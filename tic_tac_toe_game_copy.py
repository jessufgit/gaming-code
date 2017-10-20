

row1 = ['-', '-', '-'];
row2 = ['-', '-', '-'];
row3 = ['-', '-', '-'];

players = ['Player One', 'Player Two']

def askForPlayerMove():
	gameWon = False;

	while gameWon == False:
		for player in players:
			if gameWon == True:
				break;
			else:
				playerRowMove = int(input(player + ', what row?'));
				playerColMove = int(input(player + ', what column?'));
				playerColMove -= 1;

				if player == 'Player One':
					if (playerRowMove == 1 and row1[playerColMove] == '-'):
						row1[playerColMove] = 'X';
					elif (playerRowMove == 2 and row2[playerColMove] == '-'):
						row2[playerColMove] = 'X';
					elif (playerRowMove == 3 and row3[playerColMove] == '-'):
						row3[playerColMove] = 'X';
					else:
						print("That space is taken, you've lost your turn.")
					print(row1);
					print(row2);
					print(row3);

					if ((row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X') or (row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X') or (row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X') or (row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X') or (row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X') or (row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X') or (row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X') or (row1[2] == 'X' and row2[1] == 'X' and row3[0] == 'X')): 
						print("Player One (X) wins!");
						gameWon = True;
						break;

				else:
					if (playerRowMove == 1 and row1[playerColMove] == '-'):
						row1[playerColMove] = 'O';
					elif (playerRowMove == 2 and row2[playerColMove] == '-'):
						row2[playerColMove] = 'O';
					elif (playerRowMove == 3 and row3[playerColMove] == '-'):
						row3[playerColMove] = 'O';
					else:
						print("That space is taken, you've lost your turn.")
					print(row1);
					print(row2);
					print(row3);

					if ((row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O') or (row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O') or (row3[0] == 'O'and row3[1] == 'O' and row3[2] == 'O') or (row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O') or (row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O') or (row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O') or (row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O') or (row1[2] == 'O' and row2[1] == 'O' and row3[0] == 'O')):  
						print("Player Two (O) wins!");
						gameWon = True;

askForPlayerMove()
    


