#Example 2.12  => how to read a list of numbers from the keyboard.
s = input("Input a list of numbers: ")
numbers = list(map(int, s.split()))
print(numbers)