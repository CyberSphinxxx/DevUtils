import random

def roll_dice(sides=6, num_dice=1):
    """
    Rolls a specified number of dice with a specified number of sides.
    """
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, sides))
    return results

if __name__ == "__main__":
    print("Rolling 1 d6:", roll_dice())
    print("Rolling 2 d6:", roll_dice(num_dice=2))
    print("Rolling 1 d20:", roll_dice(sides=20))
