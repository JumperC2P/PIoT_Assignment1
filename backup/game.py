from json import JSONDecodeError

from sense_hat import SenseHat

from Dice import Dice
import json
import time


class Game:

    def __init__(self):
        self.__file_path = 'files/record.json'
        self.__winning_point = 30
        self.__dice = Dice()
        self.__sense = SenseHat()
        self.records = None
        try:
            with open(self.__file_path) as records:
                self.records = json.load(records)
            records.close()
        except JSONDecodeError:
            print('No records.')
        except FileNotFoundError:
            f = open(self.__file_path, "x")
            f.close()

    def run(self):
        score_player1 = 0
        score_player2 = 0
        self.show_instructions()
        is_p1 = True
        is_p2 = False
        start_time = time.time()
        while True:

            if is_p1:
                score = self.__dice.go_dice(self.__sense, 'P1')
                if score is None:
                    continue

                print('p1 score:' + str(score))

                if score + score_player1 > score_player1:
                    is_p1 = False
                    is_p2 = True
                    score_player1 = score + score_player1
                    print('P1: ' + str(score_player1))

            if is_p2:
                score = self.__dice.go_dice(self.__sense, 'P2')

                if score is None:
                    continue

                print('p2 score:' + str(score))

                if score + score_player2 > score_player2:
                    is_p1 = True
                    is_p2 = False
                    score_player2 = score + score_player2
                    print('P2: ' + str(score_player2))

            if score_player1 >= 30 or score_player2 >= 30:
                break

        self.__sense.show_message('The winner is:')
        if score_player1 >= 30 and score_player2 < 30:
            self.__sense.show_message('P1')

        elif score_player1 < 30 and score_player2 >= 30:
            self.__sense.show_message('P2')
        else:
            if score_player1 > score_player2:
                self.__sense.show_message('P1')
            elif score_player1 < score_player2:
                self.__sense.show_message('P2')

        self.save_the_result(score_player1, score_player2)

    def save_the_result(self, score_player1, score_player2):
        record = dict()
        record['player2'] = score_player2
        record['player1'] = score_player1

        try:
            if self.records is not None:
                with open(self.__file_path, 'w+') as file:
                    scores = list(self.records['records'])
                    scores.append(record)
                    self.records['records'] = scores
                    file.seek(0)
                    file.write(json.dumps(self.records))
                file.close()
            else:
                raise AttributeError()
        except (JSONDecodeError, AttributeError):
            records = dict()
            records['records'] = list()
            records['records'].append(record)
            with open(self.__file_path, 'r+') as file:
                file.write(json.dumps(records))
            file.close()

    def show_instructions(self):
        print('go')
        # self.__sense.show_message('TWO players. Shake the Pi one by one. The first player who gets above 30 points wins the game.')


if __name__ == '__main__':
    game = Game()
    game.run()
