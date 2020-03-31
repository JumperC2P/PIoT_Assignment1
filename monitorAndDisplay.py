from sense_hat import SenseHat
import json


class MonitorAndDisplay:

    def __init__(self):
        """Constructer to prepare some initial data from config.json"""
        with open('files/config.json') as file:
            self.__data = json.load(file)
            self.__sense = SenseHat()
            self.__r = (255, 0, 0)
            self.__g = (0, 255, 0)
            self.__b = (0, 0, 255)

    def run(self):
        """Get the temperature and display on the scree"""
        current_temp = self.__sense.get_temperature()
        tempH = self.__sense.get_temperature_from_humidity()
        tempP = self.__sense.get_temperature_from_pressure()
        self.show_temp(round((current_temp+tempH+tempP)/3,2))
        
    def show_temp(self, temp):
        """
        Show different colour messages based on the temperature

        --------------------------------------------------------
        Parameters:

                temp:
                    the temperature you detect.

        """
        msg = 'Temperature: ' + str(temp)
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
