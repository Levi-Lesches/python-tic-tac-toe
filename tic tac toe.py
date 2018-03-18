from my_mod import veripy, is_even
length = [0, 1, 2]
board = [list ("?" * 3) for n in length]
players = ["X" , "O"]
def print_board ():	print ("\n".join ([" ".join ([cell for cell in row]) for row in board]))
def get_winner (): return [player for player in players if any (any (all (cell == player for cell in sub_list) for sub_list in combo) for combo in [[[[board [row] [cell] for cell in length if cell == col] [0] for row in length] for col in length], board]) or any (all (cell == player for cell in diagonal) for diagonal in [[board [x] [x] for x in length], [board [0 + x] [2 - x] for x in length]])]
def main ():
	input ("Decide who will be X and who will be O (X goes first). Then press Enter.")
	turn = 1
	while not get_winner(): 
		print_board()
		player = "O" if is_even (turn) else "X"
		print ("Player %s's turn." % player)
		while True:
			col = veripy (int, "Which column?", [1, 2, 3]) - 1
			row = veripy (int, "Which row?", [1, 2, 3]) - 1
			if board [row] [col] == "?": break
			print ("That spot is already taken by %s. Try another spot." % board [row] [col])
		board [row] [col] = player
		turn += 1
	print_board()
	print ("\n" + get_winner() [0] + " won the game!")
main ()