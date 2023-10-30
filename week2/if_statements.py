# Activity 1: IF statement

type = input("What type of book is this?\n")
if type == "adventure":
    print(f"\nI like {type} books!\n")
print("Finished reading book.")

#############################################
# Activity 2: IF...ELSE statement

activity = input("Please enter the activity to be performed.\n")
if activity == "calculate":
    print(f"\nPerforming calculations...\n")
else:
    print("Performing activity...")
print("Activity completed!")

###########################################
# Activity 3: IF...ELIF...ELSE statement

direct = input("Towards which direction should I go (up, down, left or right)?\n")
if direct == "up":
    print("I am moving in an upwards direction!")
elif direct == "down":
    print("I am moving in a downwards direction!")
elif direct == "left":
    print("I am moving in a left direction!")
else:
    print("I am moving in a right direction!")