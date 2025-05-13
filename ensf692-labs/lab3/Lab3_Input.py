# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
print('\n')
print("***METHOD 1***")
input1 = input("Please enter your name: ")
print("This is the first input:", input1)


# Input Method 2
print('\n' * 2)
print("***METHOD 2***")
loop = True
while loop:
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        print("This is the second input: " + input2)
        loop = False
    else:
        print("This is not the input I am looking for. Please try again.")

    



# Rewrite Input Method 2 so that no break statement is necessary 
