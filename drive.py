'''
In This File I Try to solve de Columbia CSMM.101x couse about
Articifial Inteligence.

Week 2 and 3:  
In this assignment you will create an agent to solve the n-puzzle game
 (i.e. the 8-puzzle  game generalized to an n × n array). 
You may visitmypuzzle.org/sliding for a refresher of the rules
 of the game. You will implement and compare several search
 algorithms and collect some statistics related to their performances.

'''

import math
import random as rnd
import string

class nboard(object):
    '''
    This class will represent a nxn board of a n²-1 game
    '''
    def __init__(self, size):
        '''Will initialize the board, will set it size and
        the numbers up to n*n-1 in a 2d array to represent the board.

        - self.size is the size of the board (n)
        - self.numbers are all the numbers in the board
        - self.numbers is a 2d empty array

        '''
        n=size
        
        self.size = size
        
        self.numbers = list(range(n*n))

        self.board = [[0 for x in range(n)] for y in range(n)]

        self.zero = [0,0] #This variable keeps track of the zero,
        #or null space in the board.

        self.moves_made = [] #This list will keep track of the moves
        #that were already made

    def make_board(self, num_order):
        '''
        num_order - List with n² numbers from 0 to n²-1
        Get the list of numbers and put them in order in the
        2 array of the self.board

        It will also save the position of the 0 function
        in self.zero

        Returns the Board mounted.
        '''
        n = self.size
        
        for i in range(n):
            for j in range(n):
                
                self.board[i][j] = num_order[n*i+j]
                #Getting to a new lane adds n to the index
                
                if num_order[n*i+j] == 0: #Tracking the zero
                    self.zero = [i,j]

        return self.board


    def get_board(self):
        ''' Returns the board'''
        return self.board

    def get_zero(self):
        ''' Returns the position of the zero'''

        return self.zero

    def get_numbers(self):
        ''' Returns all the numbers in the board ordered'''

        return self.numbers

    def get_moves_made(self):
        '''Returns all the moves made'''
        return self.moves_made


    
    def print_board(self):
        ''' Print the board '''
        n = self.size
        for j in range(n):
            print(self.board[:][j])

        return None



    def get_list(self):
        '''
        Returns the numbers in the board as a list from
        left to right, top to bottom
        '''
        n = self.size
        board = self.get_board()
        board_seq = [] #Will save the seq of numbers in the board
        for i in range(n):
            for j in range(n):
                board_seq.append(board[i][j])

        return board_seq
    
    def is_complete(self):
        ''' 
        Verifies if the board is in the right order, if
        it is, returns True.
        '''

        board_seq = self.get_list()
        
        if board_seq == self.get_numbers():
            return True


        return False


    def __eq__(self, other):

        '''
        Given another board, verify if the order
        of the numbers is the same, i.e., if they
        are in the same state
        '''

        if self.get_list() == other.get_list():
            return True

        return False
    
    def move_up(self):
        '''
        Moves the zero to the line above, if possible.
        Otherwise does nothing

        returns nothing
        '''
        zero_line = self.get_zero()[0]
        zero_column = self.get_zero()[1]

        board = self.get_board()
        
        if zero_line > 0: 
            #Get the number in the line above:
            num_above = board[zero_line-1][zero_column]

            #Change the place of the zero by that number
            self.board[zero_line][zero_column] = num_above

            #Change the number above for zero
            self.board[zero_line-1][zero_column] = 0

            #Updates the position of the zero
            self.zero = [zero_line-1, zero_column]

            self.moves_made.append("Up")
            
        return None


    
    
    def move_down(self):
        '''
        Moves the zero to the line below, if possible.
        Otherwise does nothing

        returns nothing        
        '''
        zero_line = self.get_zero()[0]
        zero_column = self.get_zero()[1]
        n = self.size
        board = self.get_board()
        
        if zero_line < n-1: 
            #Get the number in the line below:
            num_below = board[zero_line+1][zero_column]

            #Change the place of the zero by that number
            self.board[zero_line][zero_column] = num_below

            #Change the number below for zero
            self.board[zero_line+1][zero_column] = 0
        
            #Updates the position of the zero
            self.zero = [zero_line+1, zero_column]

            self.moves_made.append("Down")
            
        return None


    
    def move_right(self):
        '''
        Moves the zero to the right, if possible.
        Otherwise does nothing

        returns nothing
        '''
        zero_line = self.get_zero()[0]
        zero_column = self.get_zero()[1]
        n = self.size
        board = self.get_board()
        
        if zero_column < n-1: 
            #Get the number in the column to the right:
            num_right = board[zero_line][zero_column+1]

            #Change the place of the zero by that number
            self.board[zero_line][zero_column] = num_right

            #Change the number below for zero
            self.board[zero_line][zero_column+1] = 0
        
            #Updates the position of the zero
            self.zero = [zero_line, zero_column+1]

            self.moves_made.append("Right")
            
        return None


    
    def move_left(self):
        
        '''
        Moves the zero to the right, if possible.
        Otherwise does nothing

        returns nothing
        '''
        zero_line = self.get_zero()[0]
        zero_column = self.get_zero()[1]
        n = self.size
        board = self.get_board()
        
        if zero_column > 0: 
            #Get the number in the column to the right:
            num_left = board[zero_line][zero_column-1]

            #Change the place of the zero by that number
            self.board[zero_line][zero_column] = num_left

            #Change the number below for zero
            self.board[zero_line][zero_column-1] = 0
        
            #Updates the position of the zero
            self.zero = [zero_line, zero_column-1]
            self.moves_made.append("Left")
        return None

    

    def one_move(self, move_string):
        '''
        Make a move in the board given a move from the list:
        "Up", "Down", "Right", "Left"
        '''

        move = move_string.lower() #Get the string in lowercase

        if move == "up":
            self.move_up()

        
        if move == "down":
            self.move_down()

        if move == "right":
            self.move_right()

        if move == "left":
            self.move_left()


        return None


    

    def moves(self, move_list):
        '''
        Given a list of moves as in strings (Such as in the
        method above), it makes all those moves in order from first
        to last

        Returns None
        '''

        for move in move_list:
            self.one_move(move)


        return None
        


    
    def possible_moves(self):
            '''
            Given the state of the board returns a list
            of strins of the possible moves:
            "Up", "Down", "Left", "Right"
            '''
            

            possible_moves = []
            n = self.size
            zero_line = self.get_zero()[0]
            zero_column = self.get_zero()[1]

            #If the zero is not in the first line
            if zero_line > 0:
                possible_moves.append("Up")

            #If the zero is not in the last line
            if zero_line < n-1:
                possible_moves.append("Down")

            #If the zero is not in the first column
            if zero_column > 0:
                possible_moves.append("Left")

            #If the zero is not in the last column
            if zero_column < n-1:
                possible_moves.append("Right")



            possible_moves.sort()
            

            return possible_moves


        
    def newboard_move(self, move_string):
        '''
        Creates a New Board equal to 'self',
        makes the move in this board and returns it
        '''

        n = self.size
        
        #Makes the board the same size
        new_board = nboard(n)
        
        #set it in the same configuration
        new_board.make_board(self.get_list())

        #Pass on the moves made
        new_board.moves_made = self.get_moves_made()

        #Make the move
        new_board.one_move(move_string)
        

        return new_board
            





from collections import deque

def board_bfs(board):
    '''
    Applies Breadth First Search in de n-puzzle problem.
    Get the board object defined above as input, from it
    creates a tree from children boards of de avaiable moves.

    '''
    pass
