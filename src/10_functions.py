# Write a function is_even that will return true if the passed-in number is even.

def evenOrNot(num):
    # Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)

    # Print out "Even!" if the number is even. Otherwise print "Odd"
    # YOUR CODE HERE
    if num % 2 is 0:
        print('Even')
    else:
        print('Odd')
evenOrNot(5)

