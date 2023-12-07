# Example 2.12  => how to read a list of numbers from the keyboard.
s = input("Input a list of numbers: ") # reads the numbers as text into a variable called s
numbers = list(map(int, s.split())) # split()function to split it into a number of pieces , map each piece into an integer
print(numbers)