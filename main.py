import tkinter as tk

import rsa_encryption
import nth_fib
import sorting
import brute_force_merge
import random_deck
import factorial_calc
import search
import palindrome




class GUI:
    
    #=== All GUI Tasks ===#
    def __init__(self, root):
        self.root =  root
        self.setup_window()

    def show_frame(frame):
        frame.tkraise()

        
    def setup_window(self):
        self.root.title("Summative Assignment")
        self.root.geometry("1080x720")



    #Creates a button that can be clicked to access anything (self, text, colour, position x, position y, command)
    def create_button(self, text, colour, x_pos, y_pos, command):

        button = tk.Button(self.root, text=text,bg_colour=colour, command=command )
        #Change to grid format later
        button.place(x=x_pos,y=y_pos)


    def create_label(self):
        pass

    def create_entry(self):
        pass
    


    #=== Implementation of all required Algorithms ===#

    ##RSA
    def rsa_encryption_gui(self):
        pass

    ##Dynamic Programminga
    def nth_fib_gui(self):
        pass

    ##Sorting
    def sorting_gui(self):
        pass

    ##Brute Force
    def brute_force_gui(self):
        pass

    ##Randomised
    def random_deck_gui(self):
        pass

    ##Recursion
    def factorial_calculator_gui(self):
        pass

    ##Search
    def search_gui(self):
        pass

    ##Dynamic Programming
    def palindrome(self):
        pass
    
    #== Design Patterns ==#
    


