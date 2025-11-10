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
        
    def setup_window(self):
        self.root.title("Summative Assignment")
        self.root.geometry("1080x720")

    def show_frame(self, frame):
        frame.tkraise()

    def all_guis(self):
        self.rsa_encryption_gui()
        self.nth_fib_gui()
        self.sorting_gui()
        self.brute_force_gui()
        self.random_deck_gui()
        self.factorial_calculator_gui()
        self.search_gui()
        self.palindrome_gui()


    #Creates a button that can be clicked to access anything (self, text, colour, position x, position y, command)
    def create_button(self, text, x_pos, y_pos, command, colour, parent):
        button = tk.Button(parent, text=text,bg=colour, command=command )
        #Change to grid format later
        button.place(x=x_pos,y=y_pos)

    def create_label(self, text, x_pos, y_pos, parent, font_size=12):
        label=tk.Label(parent, text=text, font=("Arial",font_size))
        label.place(x=x_pos,y=y_pos)

    def create_entry(self,x_pos, y_pos, parent):
        entry=tk.Entry(parent, x_pos, y_pos, width=30)
        entry.place(x=x_pos,y=y_pos)
        return entry


    #Sidebar Implementation
    """Allows the User to easily navigate between the different algorithms implemented"""
    def sidebar(self, parent)

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
    def palindrome_gui(self):
        pass
    
    #== Design Patterns ==#
    

def main():
    root=tk.Tk()
    app=GUI(root)
    app.all_guis()
    root.mainloop()

if __name__ == "__main__":
    main()

