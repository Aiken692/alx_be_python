# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row of the pattern
while row < size:
    # Use a for loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after completing the current row
    print()
    # Increment the row counter
    row += 1
