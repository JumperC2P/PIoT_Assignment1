from json import JSONDecodeError

from sense_hat import SenseHat

from Dice import Dice
import json
import time
import datetime


class Game:

    def __init__(self):
        """
            inititalize all the variables used in the program
        """
        self.__file_path = 'files/winner.csv'
        self.__winning_point = 30
        self.__dice = Dice()
        self.__sense = SenseHat()
        self.records = None
        # preload the winner.csv file to check whether it is exist
        try:
            f = open(self.__file_path, "r")
            if len(f.read()) == 0:
                f.close()
                f = open(self.__file_path, "w")
                f.write("Time, Winner, Player1_Score, Player2_Score\n")
                f.close()
        except FileNotFoundError:
            f = open(self.__file_path, "w");
            f.write("Time, Winner, Player1_Score, Player2_Score\n")
            f.close()

    def run(self):
        score_player1 = 0
        score_player2 = 0
        self.show_instructions()
        is_p1 = True
        is_p2 = False
        start_time = time.time()
        while True:

            # Player1 roll
            if is_p1:
                score = self.__dice.go_dice(self.__sense, 'P1')
                if score is None:
                    continue

                time.sleep(1.5)
                # make sure the score is recorded.
                if score + score_player1 > score_player1:
                    # switch the player from player1 to player2
                    is_p1 = False
                    is_p2 = True
                    score_player1 = score + score_player1
                    self.__sense.show_message('P1: ' + str(score_player1))

            # Player2 roll
            if is_p2:
                score = self.__dice.go_dice(self.__sense, 'P2')
                if score is None:
                    continue

                time.sleep(1.5)
                # make sure the score is recorded.
                if score + score_player2 > score_player2:
                    # switch the player from player2 to player1
                    is_p1 = True
                    is_p2 = False
                    score_player2 = score + score_player2
                    self.__sense.show_message('P2: ' + str(score_player2))

            if score_player1 >= self.__winning_point or score_player2 >= self.__winning_point:
                time.sleep(2)
                break

        # Check who is the winner or it's a tie.
        winner = ""
        self.__sense.show_message('The winner is:')
        if score_player1 >= self.__winning_point > score_player2:
            winner = "P1"
        elif score_player1 < self.__winning_point <= score_player2:
            winner = "P2"
        else:
            if score_player1 > score_player2:
                winner = "P1"
            elif score_player1 < score_player2:
                winner = "P2"
            elif score_player1 == score_player2:
                winner = "Tie"

        # show the winner message
        self.__sense.show_message(winner)

        # save the result to winner.csv file.
        self.save_the_result(winner, score_player1, score_player2)

    def save_the_result(self, winner, score_player1, score_player2):
        """
        Save the result to winner.csv
        ---------------------------

        Parameters:
            winner:
                Winner

            score_player1:
                the score of player1

            score_player2:
                the score of player2
        """
        current_time = datetime.datetime.now()
        with open(self.__file_path, "a") as records:
            records.write("{},{},{},{} \n".format(current_time, winner, score_player1, score_player2))

    def show_instructions(self):
        """Show instruction on the screen"""
        self.__sense.show_message('TWO players. Get '+str(self.__winning_point)+' points to win.')


if __name__ == '__main__':
    game = Game()
    game.run()
