from sense_hat import SenseHat
import random
import time


class Dice:

    def __init__(self):
        # setup the threshold for shaking
        self.__threshold = 1

    def roll(self, sense):
        """
        Get the dice
        ------------

        Parameters:

            sense:
                sense hat object
        """
        # get the random number from 1 to 6
        # then, based on the number, display different images
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
        # return the number
        return number

    def go_dice(self, sense, player):
        """
        Do dicing
        -----------

        Parameters:

                sense:
                    sense hat object
                player:
                    which player is playing now
        """

        # set up to use accelerometer on sense hat
        sense.set_imu_config(False, False, True)
        # get the parameters from sense hat
        p, r, y = sense.get_accelerometer_raw().values()
        time.sleep(0.1)
        p1, r1, y1 = sense.get_accelerometer_raw().values()

        old_p = abs(p)
        old_r = abs(r)
        old_y = abs(y)

        new_p = abs(p1)
        new_r = abs(r1)
        new_y = abs(y1)

        # compare the old parameters with new parameters
        # if the difference is larger than the threshold set before, call roll function to show images
        if abs(old_p - new_p) > self.__threshold or abs(old_r - new_r) > self.__threshold or abs(old_y - new_y) > self.__threshold:
            # clear the display on hat
            sense.clear()
            next_roll = False
            start_point = time.time()
            # This is for game to display who is the current player
            if player is not None:
                sense.show_message(player)
            return self.roll(sense)

        else:
            return None
