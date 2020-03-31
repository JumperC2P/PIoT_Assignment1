from sense_hat import SenseHat
import json


class MonitorAndDisplay:

    def __init__(self):
        with open('files/config.json') as file:
            self.__data = json.load(file)
            self.__sense = SenseHat()
            self.__r = (255, 0, 0)
            self.__g = (0, 255, 0)
            self.__b = (0, 0, 255)

    def run(self):
        current_temp = int(self.__sense.get_temperature())
        msg = 'Temperature: ' + str(current_temp)
        if current_temp <= self.__data['cold_max']:
            self.__sense.show_message(msg, text_colour=self.__b)
        elif self.__data['comfortable_min'] < current_temp <= self.__data['comfortable_max']:
            self.__sense.show_message(msg, text_colour=self.__g)
        elif current_temp > self.__data['hot_min']:
            self.__sense.show_message(msg, text_colour=self.__r)
        else:
            self.__sense.show_message('Something wrong.')


if __name__ == '__main__':
    monitorAndDisplay = MonitorAndDisplay()
    while True:
        monitorAndDisplay.run()
