def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print("+" + ("-" * 7 + "+") * 3)
    for row in board:
        print(("|" + " " * 7) * 3 + "|")
        for col in row:
            print("|" + " " * 3 + str(col) + " " * 3, end="")
        print("|")
        print(("|" + " " * 7) * 3 + "|")
        print("+" + ("-" * 7 + "+") * 3)

# def EnterMove(board):
# #
# # the function accepts the board current status, asks the user about their move,
# # checks the input and updates the board according to the user's decision
# #
#
# def MakeListOfFreeFields(board):
# #
# # the function browses the board and builds a list of all the free squares;
# # the list consists of tuples, while each tuple is a pair of row and column numbers
# #
#
# def VictoryFor(board, sign):
# #
# # the function analyzes the board status in order to check if
# # the player using 'O's or 'X's has won the game
# #
#
# def DrawMove(board):
# #
# # the function draws the computer's move and updates the board
# #

# Initialize Board
board = [[col + (row * 3) for col in range(1,4)] for row in range(3)]
print(board)

board1 = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
print(board1)

DisplayBoard(board)

# def DisplayBoard(board):
# 	print("+-------" * 3,"+",sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|",sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ",end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")
#
# def EnterMove(board):
# 	ok = False	# fake assumption - we need it to enter the loop
# 	while not ok:
# 		move = input("Enter your move: ")
# 		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
# 		if not ok:
# 			print("Bad move - repeat your input!") # no, it isn't - do the input again
# 			continue
# 		move = int(move) - 1 	# cell's number from 0 to 8
# 		row = move // 3 	# cell's row
# 		col = move % 3		# cell's column
# 		sign = board[row][col]	# check the selected square
# 		ok = sign not in ['O','X']
# 		if not ok:	# it's occupied - to the input again
# 			print("Field already occupied - repeat your input!")
# 			continue
# 	board[row][col] = 'O' 	# set '0' at the selected square
#
# def MakeListOfFreeFields(board):
# 	free = []	# the list is empty initially
# 	for row in range(3): # iterate through rows
# 		for col in range(3): # iterate through columns
# 			if board[row][col] not in ['O','X']: # is the cell free?
# 				free.append((row,col)) # yes, it is - append new tuple to the list
# 	return free
#
#
# def VictoryFor(board,sgn):
# 	if sgn == "X":	# are we looking for X?
# 		who = 'me'	# yes - it's computer's side
# 	elif sgn == "O": # ... or for O?
# 		who = 'you'	# yes - it's our side
# 	else:
# 		who = None	# we should not fall here!
# 	cross1 = cross2 = True  # for diagonals
# 	for rc in range(3):
# 		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
# 			return who
# 		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
# 			return who
# 		if board[rc][rc] != sgn: # check 1st diagonal
# 			cross1 = False
# 		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
# 			cross2 = False
# 	if cross1 or cross2:
# 		return who
# 	return None
#
# def DrawMove(board):
# 	free = MakeListOfFreeFields(board) # make a list of free fields
# 	cnt = len(free)
# 	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
# 		this = randrange(cnt)
# 		row, col = free[this]
# 		board[row][col] = 'X'
#
# board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
# board[1][1] = 'X' # set first 'X' in the middle
# free = MakeListOfFreeFields(board)
# humanturn = True # which turn is it now?
# while len(free):
# 	DisplayBoard(board)
# 	if humanturn:
# 		EnterMove(board)
# 		victor = VictoryFor(board,'O')
# 	else:
# 		DrawMove(board)
# 		victor = VictoryFor(board,'X')
# 	if victor != None:
# 		break
# 	humanturn = not humanturn
# 	free = MakeListOfFreeFields(board)
#
# DisplayBoard(board)
# if victor == 'you':
# 	print("You won!")
# elif victor == 'me':
# 	print("I won")
# else:
# 	print("Tie!")