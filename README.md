# Word Counter

This is a simple Python script that counts the number of words in a text. The text can be inputted directly or read from a file.

## Functions

- `counting(value)`: This function takes a string, splits it into words, and prints the number of words. It then asks the user if they want to continue. If the user inputs 'Y', the `choice()` function is called.

- `choice_selection(choice)`: This function takes an integer as input. If the input is 1, it asks for a filename, attempts to open the file, and passes the file's contents to the `counting()` function. If the input is 2, it asks for a text input and passes it to the `counting()` function. If the input is neither 1 nor 2, it prints "Invalid Input".

- `choice()`: This function asks the user to input a choice (1 to input a file, 2 to enter text), and passes this choice to the `choice_selection()` function.

The script starts by calling the `choice()` function.

## How to Run

To run the script, simply navigate to the directory containing the script and type `python script_name.py` in your terminal, replacing `script_name.py` with the name of the Python script.

## Note

Please ensure that the file you want to read from is in the same directory as the Python script, or provide the full path to the file.
