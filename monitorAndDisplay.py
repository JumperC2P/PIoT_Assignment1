from sense_hat import SenseHat
import json
import time


class MonitorAndDisplay:

    def __init__(self):
        """Constructor to prepare some initial data from config.json"""

        self.__sense = SenseHat()
        # 3 different color for different range of temperature.
        self.__r = (255, 0, 0)
        self.__g = (0, 255, 0)
        self.__b = (0, 0, 255)

        try:
            # read the config.json and save into __data
            with open('files/config.json') as file:
                self.__data = json.load(file)
            try:
                # check the content of config.json is valid or not.
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
        """
        Check the config.json is valid or not.

        ---------------------------------------------

        """

        # check the file is loaded or not.
        if not self.__data:
            raise FileNotFoundError("The file is not loaded yet.")

        # check the file contains all the attributes needed or not.
        try:
            if not self.__data['cold_max']:
                raise AttributeError("The format of the json file is wrong, which is not ""cold_max"".")
            elif not self.__data['comfortable_min']:
                raise AttributeError("The format of the json file is wrong, which is not ""comfortable_min"".")
            elif not self.__data['comfortable_max']:
                raise AttributeError("The format of the json file is wrong, which is not ""comfortable_max"".")
            elif not self.__data['hot_min']:
                raise AttributeError("The format of the json file is wrong, which is not ""hot_min"".")

            # check whether the type of all the values is int.
            try:
                i = int(self.__data['cold_max'])
                i = int(self.__data['comfortable_min'])
                i = int(self.__data['comfortable_max'])
                i = int(self.__data['hot_min'])
            except ValueError as ve:
                wrong_input = str(ve)[str(ve).index(":") + 1::]
                raise ValueError("One of the values is not a number, which is :" + wrong_input)

        except KeyError as ke:
            raise AttributeError(
                "The format of the json file is wrong, which doesn't contain the attribute: " + str(ke))

    def run(self):
        """Get the temperature and display on the scree"""

        # Get temperatures using different sources.
        current_temp = self.__sense.get_temperature()
        tempH = self.__sense.get_temperature_from_humidity()
        tempP = self.__sense.get_temperature_from_pressure()

        # use the average to display on the screen.
        self.show_temp(round((current_temp + tempH + tempP) / 3, 2))

    def show_temp(self, temp):
        """
        Show different colour messages based on the temperature

        --------------------------------------------------------
        Parameters:

                temp:
                    the temperature you detect.

        """
        msg = 'Temp now:' + str(temp)
        if temp <= self.__data['cold_max']:
            self.__sense.show_message(msg, text_colour=self.__b)
        elif self.__data['comfortable_min'] < temp <= self.__data['comfortable_max']:
            self.__sense.show_message(msg, text_colour=self.__g)
        elif temp > self.__data['hot_min']:
            self.__sense.show_message(msg, text_colour=self.__r)
        else:
            self.__sense.show_message('Something wrong.')


if __name__ == '__main__':
    monitorAndDisplay = MonitorAndDisplay()
    while True:
        monitorAndDisplay.run()
        time.sleep(10)
