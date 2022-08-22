"""
Workshop: Random Pizza Generator
Goal: Print pizza options for the user and randomly select items from the data structures (lists, tuples, and dictionaries) to create a random pizza!
"""
# import libraries
import random

# pizza lists
crust = []  
meat = [] 
veggie = []
surprise = []  # optional extra list

# message to users
print("Welcome to Random Pizza Generator! We have the following selections: ")
# print lists for user

#Ask user to press "Enter"
input("Press Enter to generate a random pizza.") #dont need a variable because the user's input is not used else where in the code

# generate a random index position

# generate a random item for each list
selected_meat = ""
selected_veggie = ""
selected_crust = ""

# message to users
print("Your random pizza is:")
print(selected_meat, "and", selected_veggie, selected_crust, "crust pizza")

print("Enjoy!")
