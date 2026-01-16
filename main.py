import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

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
        """
        A function to setup the window title and size
        
        """
        self.root.title("Summative Assignment")
        self.root.geometry("1080x720")

    def show_frame(self, frame):
        """
        Raises the selected frame to the front for viewing
        
        Args:
            frame (tk.Frame): The frame which needs to be raised
        """
        frame.tkraise()

    def all_guis(self):
        """
        Loads the GUI implementations for each algorithm
        
        """
        self.rsa_encryption_gui()
        self.nth_fib_gui()
        self.sorting_gui()
        self.brute_force_gui()
        self.random_deck_gui()
        self.factorial_calculator_gui()
        self.search_gui()
        self.palindrome_gui()



    def create_frame(self):
        """
        Creates all the frames needed for the GUI, setting the specific widths, heights and colours
        Includes the main menu frame, sidebar frame and all algorithm frames
        
        """
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
        """
        Configures the grid layout for a given parent widget
        
        Args:
            parent (tk.Widget): The widget that needs configuring
            rows (int): How many allocated rows there are
            columns (int): How many allocated columns there are

        """
        for row in range(rows):
            parent.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            parent.grid_columnconfigure(column, weight=1)




    #Creates a button that can be clicked to access anything (self, text, colour, position x, position y, command)
    def create_button(self, text, x_pos, y_pos, command, colour, parent,sticky=None, pad_x=5, pad_y=5):
        """
        An easy and convienient way to create buttons within the GUI
        
        Args:
            text (str): The text to be displayed on the button
            x_pos (int): The height at which the button is placed
            y_pos (int): The width at which the button is placed
            command: A command to be executed when the button is clicked
            colour (str): The background colour of the button
            parent (tk.Widget): The parent widget in which the button is placed
            sticky (str): How the button expands within its grid cell
            pad_x (int): The horizontal padding around the button
            pad_y (int): The vertical padding around the button
        """
        button = tk.Button(parent, text=text,bg=colour, command=command)
        #Change to grid format later
        if sticky:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y, sticky=sticky)
        else:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y)
        return button

    def create_label(self, text, x_pos, y_pos, parent, font_size=12):
        """
        An easy way to create labels within the GUI
        
        Args:
            text (str): The text to be displayed on the label
            x_pos (int): The height at which the label is placed
            y_pos (int): The width at which the label is placed
            parent (tk.Widget): The parent widget in which the label is placed
            font_size (int): The font size of the label text
        """
        label=tk.Label(parent, text=text, font=("Arial",font_size), bg=parent["bg"])
        label.grid(row=y_pos, column=x_pos)

    def create_entry(self,x_pos, y_pos, parent):
        """
        An easy way to create entry fields within the GUI
        
        Args:
            x_pos (int): The height at which the entry field is placed
            y_pos (int): The width at which the entry field is placed
            parent (tk.Widget): The parent widget in which the entry field is placed
        """
        entry=tk.Entry(parent, width=30)
        entry.grid(row=y_pos, column=x_pos)
        return entry


    #Welcome/Main Menu Implementation
    def main_menu(self):
        """
        The first frame the user sees when opening the program, displaying the welcome message and instructions
        
        """
        self.create_label("Welcome to the Summative Assignment", 1, 2, self.main_menu_frame, font_size=20)
        self.create_label("Please select an algorithm from the sidebar to view its implementation", 1, 3, self.main_menu_frame, font_size=14)

    #Sidebar Implementation
    def sidebar(self, parent):
        """
        The sidebar which contains all the buttons to access each algorithm frame
        
        Args:
            parent (tk.Widget): The parent widget in which the sidebar is placed
            
        """
        self.create_button("Main Menu", 0, 0 , lambda: self.show_frame(self.main_menu_frame), "lightgrey", parent, sticky="w")
        self.create_button("RSA", 0, 1 , lambda: self.show_frame(self.rsa_frame), "lightgrey", parent, sticky="w")
        self.create_button("Nth Fibonacci", 0, 2 , lambda: self.show_frame(self.fib_frame), "lightgrey", parent, sticky="w")
        self.create_button("Bubble Sort", 0, 3 , lambda: self.show_frame(self.sorting_frame), "lightgrey", parent, sticky="w")
        self.create_button("Brute Force Merge Sort", 0, 4 , lambda: self.show_frame(self.brute_force_frame), "lightgrey", parent, sticky="w")
        self.create_button("Randomised Deck", 0, 5 , lambda: self.show_frame(self.random_deck_frame), "lightgrey", parent, sticky="w")
        self.create_button("Factorial", 0, 6 , lambda: self.show_frame(self.factorial_calc_frame), "lightgrey", parent, sticky="w")
        self.create_button("Search", 0, 7 , lambda: self.show_frame(self.search_frame), "lightgrey", parent, sticky="w")
        self.create_button("Palindrome", 0, 8 , lambda: self.show_frame(self.palindrome_frame), "lightgrey", parent, sticky="w")


    """
    Below are the Individual GUI implementations for each algorithm
    Each gui function runs imported functions from their respective python files

    """

    ##RSA
    def rsa_encryption_gui(self):
        """
        Docstring for rsa_encryption_gui

        """
        pass

    ##Dynamic Programminga
    def nth_fib_gui(self):
        """
        Docstring for nth_fib_gui
        
        :param self: Description
        """
        self.create_label("Nth Fibonacci",1,0, self.fib_frame, font_size=16)
        self.create_label("Finds the Nth Fibonacci number using Dynamic Programming", 1,1, self.fib_frame)

        self.create_label("Enter a number to find the Nth Fibonacci of: ", 1,2, self.fib_frame)
        self.fib_user_entry=self.create_entry(1,3, self.fib_frame)
        
        self.fib_result_text=scrolledtext.ScrolledText(self.fib_frame,width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.fib_result_text.grid(row=5, column=1, padx=10, pady=10)

        def show_fib_results():
            try:
                user_input=int(self.fib_user_entry.get())

                result=nth_fib.fibonacci(user_input)
                self.fib_result_text.configure(state="normal")
                self.fib_result_text.delete(1.0, tk.END)
                self.fib_result_text.insert(tk.END, f"The {user_input}th Fibonacci number is:\n {result}")
                self.fib_result_text.configure(state="disabled")
            except ValueError:
                self.fib_result_text.delete(1.0, tk.END)
                messagebox.showerror("Error", "Something went Wrong. Please Try Again")

        self.create_button("Find nth Fibonacci", 1,4, lambda: show_fib_results(), "lightgrey", self.fib_frame)
        pass

    ##Sorting
    def sorting_gui(self):
        """
        Docstring for sorting_gui
        
        :param self: Description
        """
        self.create_label("Sorting Algorithms",1,0 ,self.sorting_frame, font_size=16)
        self.create_label("Select the sorting algorithm from the dropdown box below,input the numbers you would like sorted,\nand choose how you want them ordered",1,1,self.sorting_frame)

        #Dropdown Box containing the 2 sorting algorithms implemented
        algorithm_dropdown_box=ttk.Combobox(self.sorting_frame, values=["Bubble Sort", "Selection Sort"])
        algorithm_dropdown_box.current(0)
        algorithm_dropdown_box.configure(state="readonly")
        algorithm_dropdown_box.grid(row=2,column=1)

        ordering_dropdown_box=ttk.Combobox(self.sorting_frame, values=["Ascending", "Descending"])
        ordering_dropdown_box.current(0)
        ordering_dropdown_box.configure(state="readonly")
        ordering_dropdown_box.grid(row=3,column=1)

        #The users array input entry
        self.create_label("Enter the numbers to be sorted, seperated by commas: ",1,4,self.sorting_frame)
        self.sorting_user_entry=self.create_entry(1,5,self.sorting_frame)
        
        #Initalising the Ouput, a scrolled text box
        self.sorting_result_text=scrolledtext.ScrolledText(self.sorting_frame,width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.sorting_result_text.grid(row=7, column=1, padx=10, pady=10)

        def show_sorting_result():
            user_algorithm=algorithm_dropdown_box.get()
            user_input=self.sorting_user_entry.get().split(",")
            user_input=[int(user_int.strip()) for user_int in user_input]
            if ordering_dropdown_box.get()=="Ascending":
                Ascending=True
            else:
                Ascending=False

            if user_algorithm == "Bubble Sort":
                sorted_array=sorting.bubble_sort(user_input,Ascending=Ascending)
            elif user_algorithm == "Selection Sort":
                sorted_array= sorting.selection_sort(user_input,Ascending=Ascending)
            
            print(sorted_array)
            #Displaying the result on the Scrolled Text box
            self.sorting_result_text.configure(state="normal")
            self.sorting_result_text.delete(1.0, tk.END)
            format_array= ", ".join([str(i) for i in sorted_array])
            self.sorting_result_text.insert( tk.END, format_array)
            self.sorting_result_text.configure( state="disabled")
        
        #Submit Entry Button
        self.create_button("Sort Array", 1,6, lambda: show_sorting_result(), "lightgrey", self.sorting_frame)


            

        pass

    ##Brute Force
    def brute_force_gui(self):
        """
        Docstring for brute_force_gui
        
        :param self: Description
        """
        self.create_label("Merge Sort Algorithm",1,0 ,self.brute_force_frame, font_size=16)
        self.create_label("An implementation of the merge sort that using divide and conquer to sort the array given", 1,1, self.brute_force_frame)

        self.create_label("Enter an array of numbers to be sorted, seperated by commas: ", 1,2, self.brute_force_frame)
        self.brute_force_user_entry=self.create_entry(1, 3, self.brute_force_frame)

        brute_force_ordering_dropdown_box=ttk.Combobox(self.brute_force_frame, values=["Ascending", "Descending"])
        brute_force_ordering_dropdown_box.current(0)
        brute_force_ordering_dropdown_box.configure(state="readonly")
        brute_force_ordering_dropdown_box.grid(row=4,column=1)

        self.brute_force_result_text=scrolledtext.ScrolledText(self.brute_force_frame,width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.brute_force_result_text.grid(row=6, column=1, padx=10, pady=10)

        def show_brute_force_results():
            user_input=self.brute_force_user_entry.get().split(",")
            user_input=[int(user_int.strip()) for user_int in user_input]
            if brute_force_ordering_dropdown_box.get()=="Ascending":
                Ascending=True
            else:
                Ascending=False
            
            sorted_array=brute_force_merge.merge_sort(user_input,Ascending=Ascending)

            #Displaying the result on the Scrolled Text box
            self.brute_force_result_text.configure(state="normal")
            self.brute_force_result_text.delete(1.0, tk.END)
            format_array= ", ".join([str(i) for i in sorted_array])
            self.brute_force_result_text.insert( tk.END, format_array)
            self.brute_force_result_text.configure( state="disabled")

        #Submit Entry Button
        self.create_button("Sort Array", 1,5, lambda: show_brute_force_results(), "lightgrey", self.brute_force_frame)

        pass

    ##Randomised
    def show_deck(self, unshuffled_deck):
        """
        Displays the deck of cards in the text widget
        
        Args:
            unshuffled_deck (list[str]): The list of cards to display
        """
        self.cards.configure(state='normal')
        self.cards.delete(1.0, tk.END)
        for i in range(0, len(unshuffled_deck), 13):
            row=unshuffled_deck[ i:i+13]
            self.cards.insert(tk.END, ", ".join(row)+"\n")
        self.cards.configure(state='disabled')
        
    def shuffle_deck(self, unshuffled_deck):
        """
        Runs the fisher Yates shuffle algorithm, and displays the shuffled deck to the user
        
        Args:
            unshuffled_deck (list[str]): The list of cards to shuffle and display
        """
        
        self.cards.delete(1.0, tk.END) #Removes the previous deck
        self.cards.configure(state='normal')
        shuffled_deck=random_deck.Fisher_yates_shuffle(unshuffled_deck.copy())
        self.show_deck(shuffled_deck)
        self.cards.configure(state='disabled') #Changes the scrolled text box to read only, preventing users editing it

    def random_deck_gui(self):
        """
        The specific GUI for the Randomised Deck Algorithm
        It showcases the original deck, and allows the user to then shuffle the deck using the Fisher-Yates Shuffle Algorithm
        
        """
        self.create_label("Randomised Deck of Cards",1, 0, self.random_deck_frame, font_size=16)
        self.create_label("Shuffles a standard deck of cards using the Fisher-Yates Shuffle Algorithm", 1, 1, self.random_deck_frame)
        
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

    def factorial_calculator_gui(self):
        """
        The specific GUI for the Factorial Calculator Algorithm
        Uses an entry box to get the user input, and outputs the result in a scrollable text box
        
        """
        self.create_label("Recursive Factorial Calculator",1, 0, self.factorial_calc_frame, font_size=16)
        self.create_label("Uses a recursion to find the factorials from a given number", 1, 1, self.factorial_calc_frame, font_size=12)
        self.create_label("Enter a number: ", 1,2, self.factorial_calc_frame)

        self.user_factorial_entry=self.create_entry(1,3, self.factorial_calc_frame)
        
        #Initialising Scrolled Text Box
        self.factorial_result_text=scrolledtext.ScrolledText(self.factorial_calc_frame,width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.factorial_result_text.grid(row=5, column=1, padx=10, pady=10)
        #Showing Result
        def show_factorial_result():
            try:
                #Convert Entry Object to integer type
                user_input=int(self.user_factorial_entry.get())
                #Gets the Result, and coverts it into a string
                ## This is done to allow it to be displayed in a scrolled text box
                result=str(factorial_calc.calculate_factorial(user_input))

                

                #Scrollable Result, as to avoid the window expanding beyond screen size#
                ##Deletes any previous text
                self.factorial_result_text.delete(1.0, tk.END)

                ##Specifies the length to go to until going to a new line
                wrap_length=49

                ##Inserts the result within the wrap length
                wrapping = '\n'.join([result[i:i+wrap_length] for i in range(0, len(str(result)), wrap_length)])
                self.factorial_result_text.insert(tk.END,wrapping)

                
            except ValueError:
                self.factorial_result_text.delete(1.0, tk.END)
                messagebox.showerror("Error", "Something went Wrong! Please Try Again!")
            except RecursionError:
                self.factorial_result_text.delete(1.0, tk.END)
                messagebox.showerror("Error", "The Number entered exceeded the limit of the recursion depth in Python (1000).\nPlease Enter a Smaller Number!")
        #Submit Button
        self.create_button("Calculate Factorial", 1,4,lambda: show_factorial_result(), "lightgrey", self.factorial_calc_frame)
        
    ##Search
    def search_gui(self):
        """
        The specific GUI for the search.py functions
        It uses an entry box to get the users list of numbers, and displays the releveant statistics withing a scrollable text box
        
        """
        self.create_label("Statistical Analysis", 1, 0, self.search_frame, font_size=16)
        self.create_label("Enter a list of numbers, seperated by commas, to recieve the statistics of your array", 1, 1, self.search_frame)
        self.create_label("Enter array: ", 1, 2, self.search_frame)

        self.user_search_entry=self.create_entry(1,3,self.search_frame)
        
        #Initialising Scrolled Text Box
        self.search_result_text=scrolledtext.ScrolledText(self.search_frame,width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.search_result_text.grid(row=5, column=1, padx=10, pady=10)

        #Showing Result
        def show_search_result():
            user_input=self.user_search_entry.get()
            #coverts input into a list of integers:
            user_array = [int(x.strip()) for x in user_input.split(",")]
            output=search.calculate_statistics(user_array)
            
            #Adds results to the scrollable text box
            self.search_result_text.configure(state="normal")
            self.search_result_text.delete(1.0, tk.END)

            format_output=  (
                f"""Smallest Value: {output[0]}
Largest Value: {output[1]}
Mode: {output[2]}
Median: {output[3]}
1st Interquartile Range: {output[4]}
3rd Interquartile Range: {output[5]}""")

            self.search_result_text.insert(tk.END, format_output)
            self.search_result_text.configure(state="disabled")
            
        #Submit Button
        self.create_button("Find Statistics of Array", 1,4,lambda: show_search_result(), "lightgrey", self.search_frame)

        pass


    ##Dynamic Programming
    def palindrome_gui(self):
        """
        The specific GUI for the Palindrome Substring Counter Algorithm
        It uses an entry box to get user input, and displays the result within a label
        
        """
        self.create_label("Palindrome Substring Counter", 1,0, self.palindrome_frame, font_size=16)
        self.create_label("Uses memorisation to count all the Palindrome Substrins in a given string", 1, 1, self.palindrome_frame)
        self.user_palindrome_entry= self.create_entry(1,2,self.palindrome_frame)

        def show_palindrome_results():
            user_input=self.user_palindrome_entry.get()
            result=palindrome.palindrome_substrings_count(user_input)

            self.create_label(f"There are {result} Palindrom Substrings in the given string", 1, 4, self.palindrome_frame, font_size=12)

        self.create_button("Count Palindrom Substrings", 1, 3, lambda: show_palindrome_results(), "lightgrey", self.palindrome_frame)


        pass
    
    

def main():
    root=tk.Tk()
    app=GUI(root)
    app.all_guis()
    root.mainloop()

if __name__ == "__main__":
    main()

