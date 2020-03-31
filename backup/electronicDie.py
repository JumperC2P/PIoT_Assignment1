import random
import time
from sense_hat import SenseHat

from Dice import Dice


class ElectronicDie:

    def __init__(self):
        self.__sense = SenseHat()
        self.__sense.show_message('Shake.')

    def run(self, start_point, next_roll):
        dice = Dice()
        return dice.go_dice(self.__sense, None)


if __name__ == '__main__':
    die = ElectronicDie()

    is_next = True
    start_time = time.time()
    while True:
        if is_next:
            if die.run(start_time, is_next) is not None:
                is_next = False
                start_time = time.time()

        if time.time() - start_time > 1:
            is_next = True
