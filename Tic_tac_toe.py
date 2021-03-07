#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import numpy as np

#SUPER CLASS 
class Game_board():
    def __init__(self):
        self.board = ['_', '_', '_','_', '_', '_', '_', '_', '_', '_'];
    
    #method to display board
    def display_board(self):
        print("\n")
        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3] + "     1 | 2 | 3")
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6] + "     4 | 5 | 6")
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9] + "     7 | 8 | 9")
        print("\n")  
    
    #method to update board after each move made either by human or computer
    def update_board(self, board_position, player):
        if self.board [board_position] == '_':
            self.board [board_position] = player
        else:
            print("Oops, place already occupied!!, Try another move")
            xyz = int(input("choose a place between 1-9 from the right table shown "))
            
            #object of human class called for recursion 
            human.move(xyz)
            
            
    #check for winner in all the possible winning moves
    def who_is_winner(self, player):
        if self.board[1] == player and self.board[2] == player and self.board[3] == player:
            return True
        if self.board[4] == player and self.board[5] == player and self.board[6] == player:
            return True
        if self.board[7] == player and self.board[8] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        if self.board[3] == player and self.board[6] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True 
        return False
    
    #check for tie if the board is full
    def check_for_tie(self):
        block_position = 0;
        for space in self.board:
            if space != '_':
                block_position += 1;
        if block_position == 9:
            return True
        else:
            return False
    
    #reset the board to new incase to replay the game
    def reset(self):
        self.board =[]
        self.board = ['_', '_', '_','_', '_', '_', '_', '_', '_', '_'];    
        play.refresh_screen()
                        
    
    #refresh and display the board after each move
    def refresh_screen(self):
        self.display_board()

#object of Game_board class made called play
play = Game_board()    


#CHILD CLASS that inherits Game_board class
class human_player(Game_board):
    
    #move of human denoted by X
    def __init__(self):
        self.char = "X"
    
    #method move() to assign the move to the board. Same method used in computer_player class to show polymorphism 
    def move(self, xyz):
        self.position = xyz
        play.update_board(self.position, self.char)
        
#object of human_player class made called human      
human = human_player()


#CHILD CLASS that inherits Game_board class 
class computer_player(Game_board):
    
    #move of computer denoted by O
    def __init__(self):
        self.char = "O"
    
    #method move() to assign the move to the board. Same method used in human_player class to show polymorphism 
    def move(self):
        
        #selecting random positions
        self.position = np.random.randint(1,9)
        if play.board [self.position] == '_':
            play.update_board(self.position, self.char)
        else:
            #if the random positions is occupied or not available then do recursion and call the move() method again
            comp.move()
        
#object of computer_player class made called comp        
comp = computer_player()
print("Welcome to tic-tae-toe fun game ")
play.refresh_screen()

#infinite loop
while True:
    #selecting first player randomly
    c = random.randint(0,1);
    if c == 1:
        print("User plays first move.")
    else:
        print("Computer plays first move.")
    while True:
    
        #if the random value gives 1, user plays first move
        if c == 1:
            
            #taking input from user and converting to int
            xyz = int(input("Choose a place between 1-9 from the right table shown "))
            #calling human_player class through its object by passing that int value
            human.move(xyz)
    
            #refresh screen to update and display the board
            play.refresh_screen()
    
            #check for winner: if winner, display message and ask for replay or not
            if play.who_is_winner("X"):
                print(" Congratulations User!!! You beat the computer. You win " )
                break
        
            #check for tie: if tie, display message and ask for replay or not      
            if play.check_for_tie():
                print(" Both played well and it's a Tie!!!" )
                break
            
            #calling computer_player through it's method comp by passing no value as the method calculates the random value with in  
            comp.move()
    
            #refresh screen to update and display the board
            play.refresh_screen()
    
            #check for winner: if winner, display message and ask for replay or not
            if play.who_is_winner("O"):
                print(" Congratulations computer!! you wins" )
                break 
            
            #check for tie: if tie, display message and ask for replay or not        
            if play.check_for_tie():
                print(" Both played well and it's a Tie!!! " )
                break
         
        #if the random value gives 0, computer player plays first
        elif c == 0:
            #calling computer_player through it's method comp by passing no value as the method calculates the random value with in  
            comp.move()
    
            #refresh screen to update and display the board
            play.refresh_screen()
    
            #check for winner: if winner, display message and ask for replay or not
            if play.who_is_winner("O"):
                print(" Congratulations computer!! you wins" )
                break 
            
            #check for tie: if tie, display message and ask for replay or not        
            if play.check_for_tie():
                print(" Both played well and it's a Tie!!! ")
                break;
                
            #taking input from user and converting to int
            xyz = int(input("Choose a place between 1-9 from the right table shown "))    
            human.move(xyz)
    
            #refresh screen to update and display the board
            play.refresh_screen()
    
            #check for winner: if winner, display message and ask for replay or not
            if play.who_is_winner("X"):
                print(" Congratulations User!!! You beat the computer. You win " )
                break
        
            #check for tie: if tie, display message and ask for replay or not      
            if play.check_for_tie():
                print(" Both played well and it's a Tie!!!" )
                break
                
    play_again = input(" Do you want to play again? ").upper()
    if play_again.startswith('Y'):
            
        #if want to play again use reset method to clear the board and continue the loop
            play.reset()
            continue
    else:
        break;

