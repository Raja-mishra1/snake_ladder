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

def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

def snake_ladder(player_name, current_value, dice_value,snakes):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        sys.exit(1)


    
    
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
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value,snakes)
        check_win(player1_name, player1_current_position)
        

if __name__ == "__main__":
    start()