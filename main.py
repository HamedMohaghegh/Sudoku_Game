# Import necessary modules
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Sudoku
from Sudoku import my_game
from Sudoku import my_list
from Sudoku import my_list_column
from Sudoku import new_game
from tkinter.ttk import Entry, Style

# Initialize the Sudoku game
Sudoku.new_game(my_list, my_list_column, my_game)

# Create the main window
window = tk.Tk()
style = ttk.Style(window)
window.title("Sudoku")
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
style_cell = Style()
style_cell.configure("Red.TEntry", fieldbackground="red")

# Create a frame within the window
frame = ttk.Frame(window)
frame.pack()

# Function to reveal hints in the Sudoku puzzle


def hint():
    y = 0
    for i in range(9):
        for j in range(9):
            # Get the value of the cell from the list
            value = my_game[i][j]
            # Set the StringVar object to the value
            text_vars[i][j].set(value)
            if y == 0 and value == 0:
                value = my_list[i][j]
                my_game[i][j] = value
                # Set the StringVar object to the value
                text_vars[i][j].set(value)
                y += 1
                # Create an Entry widget with the textvariable option
                entry = ttk.Entry(numbers_frame, width=1,
                                  textvariable=text_vars[i][j], font=("Arial", 16, "bold"))
                entry.grid(row=i, column=j, padx=3, pady=3)

# Function to get the numbers entered by the user and check if the puzzle is solved


def get_numbers():
    numbers = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            # Get the value of the Entry widget
            value = text_vars[i][j].get()
            # Append it to the list
            numbers[i].append(int(value))
    if numbers == my_list:
        tkinter.messagebox.showinfo(title="You Won", message="You Won")
    else:
        tkinter.messagebox.showinfo(title="You Lose", message="You Lose")


# Create a 2D list of StringVar objects to store values of Sudoku cells
text_vars = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

# Create a frame for displaying Sudoku numbers
numbers_frame = ttk.LabelFrame(frame, text="Sudoku numbers")
numbers_frame.grid(row=0, column=0, padx=20, pady=20)

# Function to clear the numbers frame


def destroy():
    children = numbers_frame.winfo_children()
    for child in children:
        child.destroy()

# Function to generate a new Sudoku puzzle


def new():
    destroy()
    global my_list
    global my_list_column
    global my_game
    # Reset Sudoku lists and generate a new game
    my_list = [[], [], [], [], [], [], [], [], []]
    my_list_column = [[], [], [], [], [], [], [], [], []]
    my_game = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    my_list = new_game(my_list, my_list_column, my_game)
    # Populate the numbers frame with the new puzzle
    for i in range(9):
        for j in range(9):
            value = my_game[i][j]
            text_vars[i][j].set(value)
            if value == 0:
                entry = ttk.Entry(numbers_frame, width=1, textvariable=text_vars[i][j],
                                  font=("Arial", 16, "bold"))
            else:
                entry = ttk.Entry(numbers_frame, width=1,
                                  textvariable=text_vars[i][j])
            entry.grid(row=i, column=j, padx=3, pady=3)


# Initialize the Sudoku puzzle on program start
new()

# Create buttons and label frame
button_label = ttk.LabelFrame(frame, text="Buttons")
button_label.grid(row=0, column=1, padx=20, pady=20, sticky="n")
button_end = ttk.Button(button_label, text="End", command=get_numbers)
button_end.grid(row=0, column=0, padx=7, pady=7)
button_hint = ttk.Button(button_label, text="Hint", command=hint)
button_hint.grid(row=2, column=0, padx=7, pady=7)
button_new = ttk.Button(button_label, text="New", command=new)
button_new.grid(row=3, column=0, padx=7, pady=7)

# Run the main loop
window.mainloop()
