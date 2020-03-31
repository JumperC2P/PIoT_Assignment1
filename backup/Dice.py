from sense_hat import SenseHat
import random
import time


class Dice:

    def __init__(self):
        self.__threshold = 1

    def roll(self, sense):
        number = random.randint(1, 6)
        if number == 1:
            sense.load_image('images/die-1.png')
        elif number == 2:
            sense.load_image('images/die-2.png')
        elif number == 3:
            sense.load_image('images/die-3.png')
        elif number == 4:
            sense.load_image('images/die-4.png')
        elif number == 5:
            sense.load_image('images/die-5.png')
        else:
            sense.load_image('images/die-6.png')
        return number

    def go_dice(self, sense, player):
        print('In Dice')
        sense.set_imu_config(False, False, True)
        p, r, y = sense.get_accelerometer_raw().values()
        time.sleep(0.1)
        p1, r1, y1 = sense.get_accelerometer_raw().values()

        old_p = abs(p)
        old_r = abs(r)
        old_y = abs(y)

        new_p = abs(p1)
        new_r = abs(r1)
        new_y = abs(y1)

        if abs(old_p - new_p) > self.__threshold or abs(old_r - new_r) > self.__threshold or abs(old_y - new_y) > self.__threshold:
            sense.clear()
            print('Go rolling')
            next_roll = False
            start_point = time.time()
            if player is not None:
                sense.show_message(player)
            return self.roll(sense)

        else:
            return None
