import tkinter as tk
from tkinter import scrolledtext

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
        self.create_frame()
        self.sidebar(self.sidebar_frame)

        self.main_menu()
        self.show_frame(self.main_menu_frame)
        
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



    def create_frame(self):
        self.configure_grid_layout(self.root, 1, 2)
        #Main menu Frame
        self.main_menu_frame=tk.Frame(self.root, bg="white")

        #Sidebar Frame
        self.sidebar_frame=tk.Frame(self.root, bg="lightgrey",width=200)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        self.sidebar_frame.grid_propagate(False)


        #Algorithm Frames
        self.rsa_frame= tk.Frame(self.root, bg="lightblue",width=880, height=720)
        self.fib_frame= tk.Frame(self.root, bg="lightgreen",width=880, height= 720)
        self.sorting_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)
        self.brute_force_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)
        self.random_deck_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)
        self.factorial_calc_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)
        self.search_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)
        self.palindrome_frame= tk.Frame(self.root, bg="lightblue", width=880, height= 720)

    
        
        #Setting frame positions
        for frame in (self.main_menu_frame, self.rsa_frame, self.fib_frame, self.sorting_frame, self.brute_force_frame,
                      self.random_deck_frame, self.factorial_calc_frame, self.search_frame, self.palindrome_frame):
            frame.grid(row=0, column=1, sticky="nsew")
        
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


    #Configuring Grid Layout
    def configure_grid_layout(self, parent, rows, columns):
        for row in range(rows):
            parent.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            parent.grid_columnconfigure(column, weight=1)




    #Creates a button that can be clicked to access anything (self, text, colour, position x, position y, command)
    def create_button(self, text, x_pos, y_pos, command, colour, parent,sticky=None, pad_x=5, pad_y=5):
        button = tk.Button(parent, text=text,bg=colour, command=command)
        #Change to grid format later
        if sticky:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y, sticky=sticky)
        else:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y)
        return button

    def create_label(self, text, x_pos, y_pos, parent, font_size=12):
        label=tk.Label(parent, text=text, font=("Arial",font_size), bg=parent["bg"])
        label.grid(row=y_pos, column=x_pos)

    def create_entry(self,x_pos, y_pos, parent):
        entry=tk.Entry(parent, width=30)
        entry.grid(row=y_pos, column=x_pos)
        return entry


    #Welcome/Main Menu Implementation
    def main_menu(self):
        self.create_label("Welcome to the Summative Assignment", 1, 2, self.main_menu_frame, font_size=20)
        self.create_label("Please select an algorithm from the sidebar to view its implementation", 1, 3, self.main_menu_frame, font_size=14)

    #Sidebar Implementation
    """Allows the User to easily navigate between the different algorithms implemented"""
    def sidebar(self, parent):
        """All Buttons needed:
        main_menu_frame,
        rsa_frame,
        fib_frame,
        sorting_frame,
        brute_force_frame,
        random_deck_frame,
        factorial_calc_frame,
        search_frame,
        palindrome_frame"""
        self.create_button("Main Menu", 0, 0 , lambda: self.show_frame(self.main_menu_frame), "lightgrey", parent, sticky="w")
        self.create_button("RSA", 0, 1 , lambda: self.show_frame(self.rsa_frame), "lightgrey", parent, sticky="w")
        self.create_button("Nth Fibonacci", 0, 2 , lambda: self.show_frame(self.fib_frame), "lightgrey", parent, sticky="w")
        self.create_button("Bubble Sort", 0, 3 , lambda: self.show_frame(self.sorting_frame), "lightgrey", parent, sticky="w")
        self.create_button("Brute Force Merge Sort", 0, 4 , lambda: self.show_frame(self.brute_force_frame), "lightgrey", parent, sticky="w")
        self.create_button("Randomised Deck", 0, 5 , lambda: self.show_frame(self.random_deck_frame), "lightgrey", parent, sticky="w")
        self.create_button("Recursion", 0, 6 , lambda: self.show_frame(self.factorial_calc_frame), "lightgrey", parent, sticky="w")
        self.create_button("Search", 0, 7 , lambda: self.show_frame(self.search_frame), "lightgrey", parent, sticky="w")
        self.create_button("Palindrome", 0, 8 , lambda: self.show_frame(self.palindrome_frame), "lightgrey", parent, sticky="w")

        
        
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
    def show_deck(self, unshuffled_deck):
        self.cards.configure(state='normal')
        self.cards.delete(1.0, tk.END)
        for i in range(0, len(unshuffled_deck), 13):
            row=unshuffled_deck[ i:i+13]
            self.cards.insert(tk.END, ", ".join(row)+"\n")
        
    def shuffle_deck(self, unshuffled_deck):
        self.cards.delete(1.0, tk.END)
        self.cards.configure(state='normal')
        shuffled_deck=random_deck.Fisher_yates_shuffle(unshuffled_deck.copy())
        self.show_deck(shuffled_deck)
        self.cards.configure(state='disabled')

    def random_deck_gui(self):
        self.create_label("Randomised Deck of Cards",1, 0, self.random_deck_frame, font_size=16)
        self.create_label("Shuffles a standard deck of cards using the Fisher-Yates Shuffle Algorithm", 1, 1, self.random_deck_frame, font_size=12)
        
        cards=random_deck.create_deck()
        #Shows original deck
        self.cards=scrolledtext.ScrolledText(self.random_deck_frame,width=90, height=10, wrap=tk.WORD, font=("Arial", 12), state="normal")
        self.cards.grid(row=2,column=0, columnspan= 4, padx=10, pady=10)
        self.show_deck(cards)
        self.cards.configure(state='disabled')


        #Shuffle Button
        self.create_button("Shuffle Deck", 1, 3, lambda: self.shuffle_deck(cards), "lightgrey", self.random_deck_frame)
        #Revert to Original Deck
        self.create_button("Revert to Original Deck", 2, 3, lambda: self.show_deck(cards), "lightgrey", self.random_deck_frame)


    ##Recursion
    def show_factoral(self, user_factorial):
        pass

    def factorial_calculator_gui(self):
        self.create_label("Recursive Factorial Calculator",1, 0, self.random_deck_frame, font_size=16)
        self.create_label("Uses a recursion to find the factorials from a given number", 1, 1, self.random_deck_frame, font_size=12)
        self.create_label("Enter a number: ", 0,2, self.factorial_calc_frame)
        self.user_factorial_entry=self.create_entry(1,2, self.factorial_calc_frame)

        #Showing result
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

