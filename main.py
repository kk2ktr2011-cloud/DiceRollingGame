import random

print("Welcome to this Dice Rolling Game!\nIn this game, you will choose a number, and the computer will roll the die as many times needed to get there\nHowever, the computer will also be playing this game, and if the computer gets a higher number in a lesser amount of rolls, then the computer wins!")

number = int(input("Please choose a number 1 - 1000: "))

computer_number = random.randint(1, 1000)

def roll_dice(target):
    num_to_get = target
    roll = random.randint(1, 6)
    

roll_dice(computer_number)
roll_dice(number)
