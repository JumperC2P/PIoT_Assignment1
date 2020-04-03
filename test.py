import json


class MonitorAndDisplay:

    def __init__(self):
        """Constructer to prepare some initial data from config.json"""
        self.__r = (255, 0, 0)
        self.__g = (0, 255, 0)
        self.__b = (0, 0, 255)

        try:
            with open('files/config.json') as file:
                self.__data = json.load(file)
            try:
             self.config_checker(self)
            except FileNotFoundError as fnfe:
                print("Something is wrong. " + str(fnfe))
            except AttributeError as ae:
                print("Something is wrong. " + str(ae))
            except ValueError as ve:
                print("Something is wrong. " + str(ve))
        except:
            print("Failed to load config.json.")

    @staticmethod
    def config_checker(self):
        if not self.__data:
            raise FileNotFoundError("The file is not loaded yet.")

        try:
            if not self.__data['cold_max']:
                raise AttributeError("The format of the json file is wrong, which is not ""cold_max"".")
            elif not self.__data['comfortable_min']:
                raise AttributeError("The format of the json file is wrong, which is not ""comfortable_min"".")
            elif not self.__data['comfortable_max']:
                raise AttributeError("The format of the json file is wrong, which is not ""comfortable_max"".")
            elif not self.__data['hot_min']:
                raise AttributeError("The format of the json file is wrong, which is not ""hot_min"".")

            try:
                i = int(self.__data['cold_max'])
                i = int(self.__data['comfortable_min'])
                i = int(self.__data['comfortable_max'])
                i = int(self.__data['hot_min'])
            except ValueError as ve:
                wrong_input = str(ve)[str(ve).index(":")+1::]
                raise ValueError("One of the values is not a number, which is :" + wrong_input)

        except KeyError as ke:
            raise AttributeError(
                "The format of the json file is wrong, which doesn't contain the attribute: " + str(ke))


#mon = MonitorAndDisplay()
#i = int("25")

try:
    f = open("files/winner.csv", "r")
    if len(f.read()) == 0:
        f.close()
        f = open("files/winner.csv", "w")
        f.write("Time, Winner, Player1_Score, Player2_Score")
        f.close()

except FileNotFoundError:
    f = open("files/winner.csv", "w")
    f.write("Time, Winner, Player1_Score, Player2_Score")
    f.close()
