import math

numbers = input("Enter the list of float numbers: ").split()
numbers = [float(num) for num in numbers]

sine_values = [math.sin(num) for num in numbers]

print("Sine values:")
for value in sine_values:
    print(value)