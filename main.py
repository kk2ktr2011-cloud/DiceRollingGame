import random, time
from functions import roll_dice_for_num_of_rolls, roll_dice_for_num

tie = False
tie_2 = False
tie_3 = False
tie_4 = False
tie_5 = False

print("Welcome to this Dice Rolling Game!\nIn this game, you will choose a number, and the computer will roll the die as many times needed to get there\nHowever, the computer will also be playing this game, and if the computer gets a higher number in a lesser amount of rolls, then the computer wins!")

print("Extra Rules:\n\tIf the numbers when rolled add up to a number greater than the target number, then the rolls will be subtracted from the total instead of added.\n\t If there are more than 20 rolls then the run for that player will end and the score will be calculated as the target number divided by 20 and then multiplied by 0.5.\n\tThe score is calculated as the target number divided by the number of rolls it took to get there.\n\tIf there is a tie, then there will be an extra round where the amount of numbers possible to pick go down.")

number = float(input("Please choose a number 1 - 100: "))

while number < 1 or number > 100:
    number = float(input("Your number was invalid, please choose a number 1 - 100: "))

computer_number = random.randint(1, 100)

print("First is the Player.")
time.sleep(1.5)
user_num_of_rolls = float(roll_dice_for_num_of_rolls(number))

print("Second is the Computer.")
time.sleep(1.5)
computer_num_of_rolls = float(roll_dice_for_num_of_rolls(computer_number))

user_roll_num = float(roll_dice_for_num(number))
computer_roll_num = float(roll_dice_for_num(computer_number))

computer_score = float(computer_number / computer_num_of_rolls)
user_score = float(number / user_num_of_rolls)

apple_user = True
apple_computer = True

while apple_user == True:
    if user_roll_num == number and user_num_of_rolls < 20:
        print(f"You rolled a {number} in {user_num_of_rolls} rolls, giving you a score of {user_score}")
        apple_user = False
    elif user_roll_num != number and user_num_of_rolls == 20:
        user_score *= 0.5
        print(f"You didn't roll a {number} in 20 rolls, but we are giving you a score of {user_score}")
        apple_user = False
    else:
        print(f"You rolled a {number} in {user_num_of_rolls} rolls, giving you a score of {user_score}")
        apple_user = False

while apple_computer == True:
    if computer_roll_num == computer_number and computer_num_of_rolls <= 20:
        print(f"The computer rolled a {computer_number} in {computer_num_of_rolls} rolls, giving it a score of {computer_score}")
        apple_computer = False
    elif computer_roll_num != computer_number and computer_num_of_rolls == 20:
        computer_score *= 0.5
        print(f"The computer didn't roll a {computer_number} in 20 rolls, but we are giving a score of {computer_score}")
        apple_computer = False

if computer_score > user_score:
   print("The computer wins!")
    
elif user_score > computer_score:
   print("You win!")
else:
    print("It's a tie!")
    tie = True

if tie == True:
    print("Since there was a tie, we will have an extra round where the amount of numbers possible to pick go down.")
    round_two = int(input("Please choose a number 1 - 50: "))
    while round_two < 1 or round_two > 50:
        round_two = int(input("Your number was invalid, please choose a number 1 - 50: "))
    computer_round_two = random.randint(1, 50)
    computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_round_two)
    user_num_of_rolls = roll_dice_for_num_of_rolls(round_two)
    user_roll_num = roll_dice_for_num(round_two)
    computer_roll_num = roll_dice_for_num(computer_round_two)
    computer_score = computer_round_two / computer_num_of_rolls
    user_score = round_two / user_num_of_rolls
    if computer_score > user_score:
        print("The computer wins!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("It's a tie again! Now, even more numbers will be taken away.")
        tie_2 = True

if tie_2 == True:
    round_three = int(input("Please choose a number 1 - 25: "))
    while round_three < 1 or round_three > 25:
        round_three = int(input("Your number was invalid, please choose a number 1 - 25: "))
    computer_round_three = random.randint(1, 25)
    computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_round_three)
    user_num_of_rolls = roll_dice_for_num_of_rolls(round_three)
    user_roll_num = roll_dice_for_num(round_three)
    computer_roll_num = roll_dice_for_num(computer_round_three)
    computer_score = computer_round_three / computer_num_of_rolls
    user_score = round_three / user_num_of_rolls
    if computer_score > user_score:
        print("The computer wins!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("It's a tie again! Now, even more numbers will be taken away.")
        tie_3 = True

if tie_3 == True:
    round_four = int(input("Please choose a number 1 - 10: "))
    while round_four < 1 or round_four > 10:
        round_four = int(input("Your number was invalid, please choose a number 1 - 10: "))
    computer_round_four = random.randint(1, 10)
    computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_round_four)
    user_num_of_rolls = roll_dice_for_num_of_rolls(round_four)
    user_roll_num = roll_dice_for_num(round_four)
    computer_roll_num = roll_dice_for_num(computer_round_four)
    computer_score = computer_round_four / computer_num_of_rolls
    user_score = round_four / user_num_of_rolls
    if computer_score > user_score:
        print("The computer wins!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("It's a tie again! Now, even more numbers will be taken away.")
        tie_4 = True

if tie_4 == True:
    round_five = int(input("Please choose a number 1 - 5: "))
    while round_five < 1 or round_five > 5:
        round_five = int(input("Your number was invalid, please choose a number 1 - 5: "))
    computer_round_five = random.randint(1, 5)
    computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_round_five)
    user_num_of_rolls = roll_dice_for_num_of_rolls(round_five)
    user_roll_num = roll_dice_for_num(round_five)
    computer_roll_num = roll_dice_for_num(computer_round_five)
    computer_score = computer_round_five / computer_num_of_rolls
    user_score = round_five / user_num_of_rolls
    if computer_score > user_score:
        print("The computer wins!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("It's a tie again! Now, even more numbers will be taken away.")
        tie_5 = True

if tie_5 == True:
    round_six = int(input("Please choose a number 1 - 3: "))
    while round_six < 1 or round_six > 3:
        round_six = int(input("Your number was invalid, please choose a number 1 - 3: "))
    computer_round_six = random.randint(1, 3)
    computer_num_of_rolls = roll_dice_for_num_of_rolls(computer_round_six)
    user_num_of_rolls = roll_dice_for_num_of_rolls(round_six)
    user_roll_num = roll_dice_for_num(round_six)
    computer_roll_num = roll_dice_for_num(computer_round_six)
    computer_score = computer_round_six / computer_num_of_rolls
    user_score = round_six / user_num_of_rolls
    if computer_score > user_score:
        print("The computer wins!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("It's a tie again! I am not doing this again, so the computer wins.")
       