import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    current_round = 1
    user_score = 0

    #Milestone #4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", current_round)

        #Milestone #1: Generate the random numbers
        computer_num = random.randint(1,100)
        user_num = random.randint(1,100)
        print("Your number is", user_num)
        
        #Milestone #2: Get user choice
        user_choice = input("Do you think your number is higher or lower than the computer's?: ")

        #Extension #1: Safeguard user input
        while user_choice not in ["higher", "lower"]:
            user_choice = input("Please enter either higher or lower: ")
        
        #Milestone #3: Write the game logic
        if (user_num > computer_num and user_choice == "higher") or (user_num < computer_num and user_choice == "lower"):
            print("You were right! The computer's number was", computer_num)
            #Milestone #5: Adding a points system
            user_score = user_score + 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)

        #Milestone #4: Play multiple rounds
        current_round = int(current_round) + 1
        print("Your score is now", user_score)
        print("")

    if user_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif user_score >= int(NUM_ROUNDS/2):
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()