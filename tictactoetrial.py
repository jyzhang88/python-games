# work in progress

# Do not delete the test board!
q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winnings = {0: q[0:3], 1: q[3:6], 2: q[6:9],
            3: q[0::3], 4: q[1::3], 5: q[2::3],
            6: q[0::4], 7: q[2:7:2]}
board = [["X", "2", "X"],
         ["X", "5", "6"],
         ["X", "8", "9"]]
lst = []
for i in range(3):
	lst.extend(board[i])
	board_row = "".join(lst)
board_row
output = "X"

for sn, ls in winnings.items():
	triplet = []
	keypoint = ""
	for lss in ls:
		triplet.append(board_row[lss])

	triplet = "".join(triplet)
	if triplet == output * 3:
		print("You've won!")
		keypoint = "Exit game"
		break
	elif sn == 7:
		print("Continue...")

keypad = {0: ["1", "2", "3"],
          1: ["4", "5", "6"],
          2: ["7", "8", "9"]}

lste = []
for key, value in keypad.items():
	lste.extend(value)

choice = ""
while str(choice) not in lste:
		choice = input("Select the digit")


for i in range(9):
	board = []


	choice = input("Select the digit")
	lst = []
	for key, value in keypad.items():
		lst.extend(value)
	if str(choice) in lst:



	lst.remove(str(choice))


def choose_first():
	import random
	turn = random.sample(["O", "X"], 1)[0]
	print("Player with {} goes first.".format(turn))

def print_board():
	for i in keypad:
		print("|".join(keypad[i]))

def check_repeat():
	lste = []
	for key, value in keypad.items():
		lste.extend(value)
	while str(choice) not in lste:
		choice = input("Please try again.")

