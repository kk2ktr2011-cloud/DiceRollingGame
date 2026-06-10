import random

print("Welcome to this Dice Rolling Game!\nIn this game, you will choose a number, and the computer will roll the die as many times needed to get there\nHowever, the computer will also be playing this game, and if the computer gets a higher number in a lesser amount of rolls, then the computer wins!")

print("Extra Rules:\n\t if the numbers when rolled add up to a number greater than the target number, then the rolls will be subtracted from the total instead of added.\n\t If there are more than 20 rolls then the run for that player will end and the score will be calculated as the target number divided by 20")

number = int(input("Please choose a number 1 - 100: "))

computer_number = random.randint(1, 100)

def roll_dice(target):
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
    
computer_num_of_roles = roll_dice(computer_number)
user_num_of_rolls = roll_dice(number)

computer_score = computer_number / computer_num_of_roles
user_score = number / user_num_of_rolls

print(f"The computer rolled a {computer_number} in {computer_num_of_roles} rolls, giving it a score of {computer_score}")
print(f"You rolled a {number} in {user_num_of_rolls} rolls, giving you a score of {user_score}")

if computer_score > user_score:
   print("The computer wins!")
    
elif user_score > computer_score:
   print("You win!")