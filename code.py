# import random database
import random

def main():
    #Define list
    generated_lottery_numbers = [0, 0, 0, 0, 0, 0, 0] 
    #Set the range for the list
    for index in range(7):   
        #Call the random function to input random numbers
        generated_lottery_numbers[index] = random.randint(0, 9) 
    for index in generated_lottery_numbers:
        #Printing the randomly generated number
        print(index,end='')  

main()