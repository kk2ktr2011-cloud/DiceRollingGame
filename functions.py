import random

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
