import random, time

def roll_dice_for_num_of_rolls(target):
    num_to_get = target
    roll = 0
    num_of_rolls = 0
    while num_of_rolls < 20:
        if roll < num_to_get:
            num_rolled = random.randint(1, 6)
            roll += num_rolled
            num_of_rolls += 1
            display_number(num_rolled)
        elif roll > num_to_get:
            num_rolled = random.randint(1, 6)
            roll -= num_rolled
            num_of_rolls += 1
            display_number(num_rolled)
        elif roll == num_to_get:
            return roll, num_of_rolls

    print("That was the last die for this player!")
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

def display_number(number):
    if number == 1:
        print("""
                _______
               |       |
               |   O   |
               |_______|
                            """)
        time.sleep(1)
    elif number == 2:
        print("""
                _______
               | O     |
               |       |
               |_____O_|
                            """)
        time.sleep(1)
    elif number == 3:
        print("""
                _______
               | O     |
               |   O   |
               |_____O_|
                            """)
        time.sleep(1)
    elif number == 4:
        print("""
                _______
               | O   O |
               |       |
               | O___O |
                            """)
        time.sleep(1)
    elif number == 5:
        print("""
                _______
               | O   O |
               |   O   |
               | O___O |
                            """)
        time.sleep(1)    
    elif number == 6:
        print("""
                _______
               | O   O |
               | O   O |
               | O___O |
                            """)
        time.sleep(1)
