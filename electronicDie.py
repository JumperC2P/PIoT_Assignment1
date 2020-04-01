import random
import time
from sense_hat import SenseHat

from Dice import Dice


class ElectronicDie:

    def __init__(self):
        """Constructor"""
        self.__sense = SenseHat()
        self.__sense.show_message('Shake.')

    def run(self):
        """Run the program and call Dice()"""
        dice = Dice()

        # Set a Boolean to check whether it can be rolled based on the dice time.
        is_next = True
        start_time = time.time()
        while True:
            if is_next:
                if dice.go_dice(self.__sense, None) is not None:
                    is_next = False
                    start_time = time.time()

            # if current time minus start time is greater than 1, then allow to roll again.
            if time.time() - start_time > 1:
                is_next = True


if __name__ == '__main__':
    die = ElectronicDie()
    die.run()
