#this program is for an ancient game "take stones"

def main():
    num_stone = 20
    current_player = "Player 1"
    next_player = "Player 2"

    while num_stone > 0:
        #to show current number of stores
        print_stone_num(num_stone)

        #player 1 or player 2 take stones
        num_take_stone = input(f"{current_player} would you like to remove 1 or 2 stones?")
        num_take_stone = int(num_take_stone)

        #make sure everyone only take 1 or 2 stones
        while num_take_stone not in [1,2]:
            num_take_stone = input("Please enter 1 or 2:")                
            num_take_stone = int(num_take_stone)
        
        #to calculate current stone number with division
        num_stone = num_stone - num_take_stone
        print("")

        #to judge if there is still stone left
        if num_stone == 0:
            print(f"{next_player} wins!")
            break

        #to change the position of player
        current_player, next_player = next_player, current_player


#to show how many stones are left
def print_stone_num(num_stone):
    print(f"There are {num_stone} stones left.")

if __name__ == '__main__':
    main()