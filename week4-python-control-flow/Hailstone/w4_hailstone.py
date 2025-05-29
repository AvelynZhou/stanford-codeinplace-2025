"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    #Step1: to get the first number from the user
    num = int(input("Enter a number: "))
    
    #Step 4: do it repeatedly
    while num!= 1:
        
        #Step2: to tell user whether it's odd or even
        remainder = num % 2 
        if remainder == 1:

            #Step3: do a calculation to the number
            num_triple = int(num * 3 + 1)
            print(f"{num} is odd, so I make 3n + 1: {num_triple}")
            num = num_triple

        else:
            num_half = int(num/2)
            print(f"{num} is even, so I take half: {num_half}")
            num = num_half

if __name__ == "__main__":
    main()