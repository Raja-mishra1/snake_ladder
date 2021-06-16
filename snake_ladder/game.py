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