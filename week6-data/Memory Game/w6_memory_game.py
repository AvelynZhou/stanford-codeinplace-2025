'''
This is a program that has a user play a memory game using lists.
It tests ability to remember and match pairs of items.
In this game the cards will be represented as numbers in a list 
and their location will be indices of the list
'''

import random

NUM_PAIRS = 3

def main():
    #Milestone1 Create the truth list
    #Use a for loop to create a list that has the values 0 through N_PAIRS-1 twice
    truths = []
    index = 0
    value = 0
    for i in range(NUM_PAIRS): 
        truths.insert(index, value)
        index += 1
        truths.insert(index, value)
        index += 1
        value += 1
    
    #Milestone2 Shuffle the list
    random.shuffle(truths)
    
    #Milestone3 Create a displayed list
    display = []
    for i in range(NUM_PAIRS *2):
        display.append('*')
    
    #Milestone 6: Play multiple turns.
    while "*" in display:
        print(display)

        #Milestone4 Get two valid indices from the user
        user_index1 = get_valid_index(display)
        user_index2 = get_valid_index(display)
        while user_index1 == user_index2:
            print("You entered the same index twice. Try again.")
            user_index2 = get_valid_index(display)

        #Milestone 5: Check correct
        value1 = truths[user_index1]  #to get the value of the truths based on the index from user
        value2 = truths[user_index2]
        if value1 == value2:  #If the values do match, update the displayed list
            display[user_index1] = value1
            display[user_index2] = value2
            print("Match!")
            clear_terminal()
        else:       #If the values don't match, display the correct answer and ask for a new try
            print(f"Value at index {user_index1} is {value1}")
            print(f"Value at index {user_index2} is {value2}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()
    
    print(display)
    print("Congratulations! You won!")

#Milestone4 Get two valid indices from the user
#this function takes in the displayed list and returns valid index user entered
def get_valid_index(display):
    while True:
        user_index = input("Enter an index: ")

        if not user_index.isdigit(): #Non-number.
            user_index =  input("Not a number. Try again.")
            continue

        user_index = int(user_index) #change user_index into number

        if user_index > (NUM_PAIRS * 2 - 1):  #Number is out-of-bounds
            user_index =  input("Invalid index. Try again.")
            continue

        if display[user_index] != "*": #Inputting an index that has already been revealed
            user_index = input("This number has already been matched. Try again.")
            continue

        return user_index


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()