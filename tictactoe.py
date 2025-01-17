#!/usr/bin/env python
# coding: utf-8

# ## Goal
# Tic Tac Toe class
# 
# Methods:
# - Load a new game
# - 2 players X and O
# - Randomise player to start
# - Display board game
# - Accept and validate moves
# - Check if any player has won

from random import randint 
import numpy as np

class TwoPlayerGame:
    def __init__(self):
        self.winner = None
        self.player1 = None
        self.player2 = None
        self.turn = None

    def welcome(self):
        '''
        prints a generic welcome message based on class name
        '''
        print(f"Welcome to the game of {self.__class__.__name__}!!")

class Tictactoe(TwoPlayerGame):
    '''
    inherits from superclass TwoPlayerGame
    '''
    def __init__(self):
        '''
        initialise a new 2-player game of TicTacToe
        '''
        super().__init__()
        self.moves = ['O', 'X']
        # initialise empty board
        self.board = { str(i+1):str(i+1) for i in np.arange(9) }

    def random_start(self):
        '''
        randomly choose a move to start
        '''
        result = randint(0,1)
        if result == 0:
            self.player1 = self.moves[0]
            self.player2 = self.moves[1]
        else:
            self.player1 = self.moves[1]
            self.player2 = self.moves[0]
        self.turn = self.player1

    def current_player(self):
        '''
        Returns the current player for current turn
        '''
        if self.player1 == self.turn:
            return "Player 1"
        else:
            return "Player 2"
            
    def update_turn(self):
        '''
        update turn to next player
        '''
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        
    def update_board(self, pos, move):
        '''
        update board with move
        '''
        self.board[pos] = move

    def validate_move(self, pos):
        '''
        validate move: (1) is a valid board position, return False if out of range
        (2) for a particular board position, 
        if the position is already filled, return False (invalid move), else True
        '''
        if pos.isdigit() and int(pos) in range(1,10):     
            if self.board[pos] not in self.moves:
                return True
        else:
            return False

    def show_board(self):
        '''
        display board
        '''
        print("-"*7)
        print(f"|{self.board['1']}|{self.board['2']}|{self.board['3']}|")
        print("-"*7)
        print(f"|{self.board['4']}|{self.board['5']}|{self.board['6']}|")
        print("-"*7)
        print(f"|{self.board['7']}|{self.board['8']}|{self.board['9']}|")
        print("-"*7)

    def check_winner(self):
        '''
        checks if there is a winner. Ends the game if
        (1) there is a winner, or
        (2) all moves are exhausted and there is no winner
        '''
        # check horizontal
        if (self.board['1'] == self.board['2'] == self.board['3']) and (self.board['1'] in self.moves):
            self.winner = self.board['1']
        if (self.board['4'] == self.board['5'] == self.board['6']) and (self.board['4'] in self.moves):
            self.winner = self.board['4']
        if (self.board['7'] == self.board['8'] == self.board['9']) and (self.board['7'] in self.moves):
            self.winner = self.board['7']
        
        # check vertical
        if (self.board['1'] == self.board['4'] == self.board['7']) and (self.board['1'] in self.moves):
            self.winner = self.board['1']
        if (self.board['2'] == self.board['5'] == self.board['8']) and (self.board['2'] in self.moves):
            self.winner = self.board['2']
        if (self.board['3'] == self.board['6'] == self.board['9']) and (self.board['3'] in self.moves):
            self.winner = self.board['3']

        # check diagonal
        if (self.board['1'] == self.board['5'] == self.board['9']) and (self.board['1'] in self.moves):
            self.winner = self.board['1']

        # check off-diagonal
        if (self.board['3'] == self.board['5'] == self.board['7']) and (self.board['3'] in self.moves):
            self.winner = self.board['3']

        # check if board is full and set winner as 'T' for a tie
        if sorted(list(set(self.board.values()))) == self.moves:
            self.winner = 'T'
        
        # check if we have a winner
        if self.winner:
            return True
        else:
            return False

    def get_winner(self):
        '''
        prints the winner/no winner message
        '''
        s = "The winner is "
        if self.winner == self.player1:
            return s+"Player 1" 
        elif self.winner == self.player2:
            return s+"Player 2" 
        else:
            return "There is no winner."

def play_game():
    '''
    Executes a game of Tic Tac Toe.
    Prints a welcome message and initialise a random player 1.
    Runs the game until we have a winner or the game ends without a winner.
    '''
    game = Tictactoe()
    game.welcome()    
    game.random_start()
    print(f"Start with player 1 using {game.player1}") 
    
    while not game.check_winner():
        # display past moves
        game.show_board()
        # get the current turn
        move = game.turn
        while 1:
            pos = input(f"{game.current_player()}'s turn. Choose your board position (pick any number displayed):")
            # validate current player's move
            if game.validate_move(pos):
                game.update_board(pos, move)
                break
            else:
                print("Invalid position. Pick only a number shown on board.")
        game.update_turn()
    
    print(f"Game over. {game.get_winner()}")

# main function when python script is executed
if __name__ == "__main__":
    play = 'Y'
    while play.upper() == 'Y':
        play_game()
        play = input("One more game??? Enter y/Y to play: ")
    print("Thank you for playing!")

