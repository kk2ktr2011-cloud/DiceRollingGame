import random

print("Welcome to this Dice Rolling Game!\nIn this game, you will choose a number, and the computer will roll the die as many times needed to get there\nHowever, the computer will also be playing this game, and if the computer gets a higher number in a lesser amount of rolls, then the computer wins!")

print("Extra Rules:\n\tIf the numbers when rolled add up to a number greater than the target number, then the rolls will be subtracted from the total instead of added.\n\t If there are more than 20 rolls then the run for that player will end and the score will be calculated as the target number divided by 20.\n\tThe score is calculated as the target number divided by the number of rolls it took to get there.")

number = int(input("Please choose a number 1 - 100: "))

while number < 1 or number > 100:
    number = int(input("Your number was invalid, please choose a number 1 - 100: "))

computer_number = random.randint(1, 100)

def roll_dice_for_num_of_rolls(target):
    num_to_get = target
    roll = 0
    num_of_rolls = 0
    while num_of_rolls < 20:
        if roll < num_to_get:
            roll += random.randint(1, 6)
            num_of_rolls += 1
        elif roll > num_to_get:
            roll -= random.randint(1, 6)
            num_of_rolls += 1
        elif roll == num_to_get:
            break
    return num_of_rolls

def roll_dice_for_num(target):
    num_to_get = target
    roll = 0
    num_of_rolls = 0
    while num_of_rolls < 20:
        if roll < num_to_get:
            roll += random.randint(1, 6)
            num_of_rolls += 1
        elif roll > num_to_get:
            roll -= random.randint(1, 6)
            num_of_rolls += 1
        elif roll == num_to_get:
            break
    return roll

computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_number)
user_num_of_rolls = roll_dice_for_num_of_rolls(number)
user_roll_num = roll_dice_for_num(number)
computer_roll_num = roll_dice_for_num(computer_number)

computer_score = computer_number / computer_num_of_rolls
user_score = number / user_num_of_rolls

apple_user = True
apple_computer = True

while apple_user == True:
    if user_roll_num == number and user_num_of_rolls <= 20:
        print(f"You rolled a {number} in {user_num_of_rolls} rolls, giving you a score of {user_score}")
        apple_user = False
    elif user_roll_num != number and user_num_of_rolls == 20:
        print(f"You didn't roll a {number} in 20 rolls, but we are giving you a score of {user_score}")
        apple_user = False

while apple_computer == True:
    if computer_roll_num == computer_number and computer_num_of_rolls <= 20:
        print(f"The computer rolled a {computer_number} in {computer_num_of_rolls} rolls, giving it a score of {computer_score}")
        apple_computer = False
    elif computer_roll_num != computer_number and computer_num_of_rolls == 20:
        print(f"The computer didn't roll a {computer_number} in 20 rolls, but we are giving a score of {computer_score}")
        apple_computer = False

if computer_score > user_score:
   print("The computer wins!")
    
elif user_score > computer_score:
   print("You win!")