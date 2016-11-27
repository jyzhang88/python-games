# work in progress

def lets_play():
	print("Welcome to the Tic-Tac-Toe!")

	# Define the variables needed
	keypad = {0: ["1", "2", "3"],
	          1: ["4", "5", "6"],
	          2: ["7", "8", "9"]}
	q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	winnings = {0: q[0:3], 1: q[3:6], 2: q[6:9],
	            3: q[0::3], 4: q[1::3], 5: q[2::3],
	            6: q[0::4], 7: q[2:7:2]}

	# Define all functions first

	def choose_first():
		import random
		global turn
		turn = random.sample(["X", "O"], 1)[0]
		print("Player with {} goes first.".format(turn))

	def print_board():
		for i in keypad:
			print("|".join(keypad[i]))

	def check_win():
		lst = []
		global keypoint
		keypoint = "string"
		for key, value in keypad.items():
			lst.extend(keypad[value])
		board_row = "".join(lst)

		for sn, ls in winnings.items():
			triplet = []

			for lss in ls:
				triplet.append(board_row[lss])

			triplet = "".join(triplet)

			if triplet == output * 3:
				print("You've won!")
				keypoint = "Exit game"
				break
			elif sn == 7:
				print("Please continute with the boring game...")

	def check_repeat():
		lste = []
		for key, value in keypad.items():
			lste.extend(value)
		while str(choice) not in lste:
			choice = input("Please try again.")

	choose_first()

	print_board()

	for i in range(9):
		if turn == "X" and i in range(9):
			choice = input("Mark the X")
			check_repeat()
		elif turn == "O" and i in range(g):
			choice = input("Mark the O")
			check_repeat()
		else:
			print("This game is a tie!")
			break

		# based on choice from above, replace number with choice
		for row in keypad:
			if choice in keypad[row]:
				new = [num.replace(choice, turn) for num in keypad[row]]
				break
		keypad[row] = new

		print_board()

		check_win()

		if keypoint == "Exit game":
			break



# Error 1: repeat number
# Error 1 Message: "The box is already filled, please pay attention!"

# Write code to play with AI
# use random number generator -> check within leftover number

