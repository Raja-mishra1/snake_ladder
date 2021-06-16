import time
import random
import sys
from conf.config import SLEEP_BETWEEN_ACTIONS,DICE_FACE,MAX_VAL,player_turn_text,snake_bite,ladder_jump,ladders

class Snake:
    def add_snake(self,start,dest):
        """[Add snake to game]

        Args:
            start ([str]): [starting point of snake]
            dest ([str]): [ending point of snake]

        Raises:
            ValueError: [description]

        Returns:
            snakes [dict]: [dictionary of snake]
        """
        snakes = dict()
        if start>dest:
            snakes[start] = dest
        else:
            raise ValueError('Snake destination greater than start point')
        return snakes
    
    def __repr__(self):
        return self.snakes
    
class Dice:

    def get_dice_value():
        """[Returns dice value]

        Returns:
            [str]: [Returns normal dice value after dice is thrown]
        """
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value

    def get_crooked_dice_value():
        """[Crokked dice returns a value after dice is thrown]

        Returns:
            [type]: [description]
        """
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randrange(2, DICE_FACE+1,2)
        print("Its a " + str(dice_value))
        return dice_value
    
def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()


    print("\nMatch will be played by'" + player1_name+"'\n")
    return player1_name

    
    
def start():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_current_position = 0
    print("Add snakes to the game")
    no_of_snakes = int(input("Enter no_of_snakes to be added to the game"))
    for i in range(no_of_snakes):
        try:
            start = input("Enter start position of snake: ")
            end = input("Enter end position of snake: ")
            snake = Snake()
            snakes = snake.add_snake(start, end)
            print(f"Added snake from {start} to {end}")
        except Exception as e:
            print(f"Error {e}")
            
    dice_type = input("Enter 1 for Crooked dice: ")
    
    for i in range(10):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice = Dice()
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        if dice_type == "1":
            dice_value = Dice.get_crooked_dice_value()
        else:
            dice_value = Dice.get_dice_value()
        

if __name__ == "__main__":
    start()