# Import the tkinter library for GUI
from tkinter import *

# Initialize the main window
win = Tk()  # Start of the application

# Global variable to store the input data
data = ""

# Function to append the clicked button's value to the input data
def get_data(value):
    global data
    data = data + str(value)  # Append the value to the existing data
    var.set(data)  # Update the display with the new data

# Function to evaluate the expression and display the result
def equal_data():
    global data
    try:
        total = str(eval(data))  # Evaluate the expression and convert to string
        var.set(total)  # Display the result
        data = ""  # Clear the data for the next input
    except:
        var.set("Error")  # Display "Error" if evaluation fails

# Function to clear the input data and reset the display
def clear():
    global data
    data = ""  # Clear the data
    var.set("")  # Clear the display

# Set the title of the window
win.title("Calculator")

# Set the background color of the window
win.config(bg="yellow")

# Set the size of the window and make it non-resizable
win.geometry("500x560")
win.resizable(False, False)

# Create a label for the calculator title
label_title = Label(win, text="Calculator",
                    font=("Times New Roman", 50, "bold"), bg="yellow")
label_title.place(x=90, y=20, height=70, width=320)

# Create a StringVar to store the input/output data
var = StringVar()

# Create an entry widget to display the input/output
entry = Entry(win, relief="sunken", font=("Times New Roman", 30, "bold"), bd=5,
              textvariable=var)
entry.place(x=20, y=110, height=60, width=460)

# Create buttons for digits 1-9, 0, and operators (+, -, *, /, .)
# Each button calls the get_data function with the corresponding value when clicked

# Row 1: Buttons for 1, 2, 3, and +
button_1 = Button(win, text="1", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(1))
button_1.place(x=20, y=190, height=70, width=115)

button_2 = Button(win, text="2", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(2))
button_2.place(x=135, y=190, height=70, width=115)

button_3 = Button(win, text="3", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(3))
button_3.place(x=250, y=190, height=70, width=115)

button_add = Button(win, text="+", font=("Times New Roman", 30, "bold"),
                    command=lambda: get_data("+"))
button_add.place(x=365, y=190, height=70, width=115)

# Row 2: Buttons for 4, 5, 6, and -
button_4 = Button(win, text="4", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(4))
button_4.place(x=20, y=260, height=70, width=115)

button_5 = Button(win, text="5", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(5))
button_5.place(x=135, y=260, height=70, width=115)

button_6 = Button(win, text="6", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(6))
button_6.place(x=250, y=260, height=70, width=115)

button_sub = Button(win, text="-", font=("Times New Roman", 30, "bold"),
                    command=lambda: get_data("-"))
button_sub.place(x=365, y=260, height=70, width=115)

# Row 3: Buttons for 7, 8, 9, and *
button_7 = Button(win, text="7", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(7))
button_7.place(x=20, y=330, height=70, width=115)

button_8 = Button(win, text="8", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(8))
button_8.place(x=135, y=330, height=70, width=115)

button_9 = Button(win, text="9", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(9))
button_9.place(x=250, y=330, height=70, width=115)

button_mult = Button(win, text="*", font=("Times New Roman", 30, "bold"),
                     command=lambda: get_data("*"))
button_mult.place(x=365, y=330, height=70, width=115)

# Row 4: Buttons for ., 0, Clear (C), and /
button_dot = Button(win, text=".", font=("Times New Roman", 30, "bold"),
                    command=lambda: get_data("."))
button_dot.place(x=20, y=400, height=70, width=115)

button_0 = Button(win, text="0", font=("Times New Roman", 30, "bold"),
                  command=lambda: get_data(0))
button_0.place(x=135, y=400, height=70, width=115)

button_clear = Button(win, text="C", font=("Times New Roman", 30, "bold"),
                      command=clear)
button_clear.place(x=250, y=400, height=70, width=115)

button_div = Button(win, text="/", font=("Times New Roman", 30, "bold"),
                    command=lambda: get_data("/"))
button_div.place(x=365, y=400, height=70, width=115)

# Row 5: Button for = (equals)
button_equal = Button(win, text="=", font=("Times New Roman", 30, "bold"),
                      command=equal_data)
button_equal.place(x=135, y=470, height=70, width=230)

# Start the main event loop
win.mainloop()  # End of the application