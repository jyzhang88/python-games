# Game of Tic-Tac-Toe

def lets_play():
	print("Welcome to the Tic-Tac-Toe! \n")

	# Define the variables needed
	keypad = {0: ["1", "2", "3"],
	          1: ["4", "5", "6"],
	          2: ["7", "8", "9"]}

	# Define the winning combinations to check against
	q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	winnings = {0: q[0:3], 1: q[3:6], 2: q[6:9],
	            3: q[0::3], 4: q[1::3], 5: q[2::3],
	            6: q[0::4], 7: q[2:7:2]}


	# Define the functions needed
	def choose_first(): # choose either X or O to go first
		import random
		turn = random.sample(["X", "O"], 1)[0]
		print("Player with {} goes first.".format(turn))
		return turn

	def print_board():  # print the board out
		for i in keypad:
			print("|".join(keypad[i]))

	def check_win():    # check if someone has won the game
		lst = []
		global keypoint
		keypoint = "string"
		for key, value in keypad.items():
			lst.extend(value)
		board_row = "".join(lst)

		for sn, ls in winnings.items():
			triplet = []

			for lss in ls:
				triplet.append(board_row[lss])

			triplet = "".join(triplet)

			# checking the board against the winning combination
			if triplet == turn * 3:
				print("{} has won!".format(turn))
				keypoint = "Exit game"
				break
			elif sn == 7:
				print("Next player's choice...")

	def check_repeat(): # check if the number is already taken
		lste = []
		for key, value in keypad.items():
			lste.extend(value)
		while True:
			global choice
			choice = input("Mark the {}".format(turn))
			if choice not in lste:
				print("Number is already used, please try again")
				continue
			else:
				break

	turn = choose_first()
	print_board()

	for i in range(9):  # enters the loop of the game
		if turn == "X" and i in range(8):
			check_repeat()
		elif turn == "O" and i in range(8):
			check_repeat()
		else:
			print("This game is a tie!")
			break

		# replacing the numbers with X or O
		for row in keypad:
			if choice in keypad[row]:
				new = [num.replace(choice, turn) for num in keypad[row]]
				break
		keypad[row] = new

		check_win()
		print_board()

		# if someone has won the game, exit out of the game loop
		if keypoint == "Exit game":
			break

		# if the game has not ended, alternate between X and O
		if turn == "X":
			turn = "O"
		elif turn == "O":
			turn = "X"
