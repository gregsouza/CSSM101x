'''
 The Functions in this file will be used to teste the n-puzzle board
I create in drive.py

'''

import random as rnd
from drive import *

#board = nboard(3)


'''
Testing Make Board, print board and is complete
'''

# #num_order = rnd.sample(num_order, len(num_order))

# board.make_board(num_order)

# print("board: \n")

# board.print_board()

# print("testing get_numbers: \n")

# print(board.get_numbers())

# print("testing is_complete()\n")

# print(board.is_complete())

'''
Testing the move methods

'''

# num_order = [1,2,3,4,6,0,5,7,8]
# board.make_board(num_order)

# print("board: \n")

# board.print_board()

# board.moves(["Up", "Left", "Left", "Down"])

# print("after the moves \n")

# board.print_board()

# print(board.get_moves_made())


'''
Testing __eq__
'''

board = nboard(3)
board2 = nboard(3)


num_order = [1,2,3,4,6,0,5,7,8]
num_order2 = [1,3,2,4,6,0,5,7,8]

board.make_board(num_order)
board2.make_board(num_order2)

print(board==board2)

