__author__ = 'Eugene Davis'

import requests

class FI8910W_wrapper:

    # User parameter to hand off to camera
    user = "";
    # Password parameter to hand off to camera
    password = ""
    # URL to camera
    url = ""

    def __init__(self, url, user, password):
        """
        Constructor, it sets the url, user and password for the camera
        :param url String URL/IP address of the camera
        :param user String administrative username for the camera
        :param password String password that goes with the administrative user
        :return;
        """
        self.url = url
        self.user = user
        self.password = password

    def __get_params__(self, command):
        """
        Generates the parameters to send to the camera, returns them in an associative array
        """
        params = {"user":self.user, "pwd":self.password, "command":command}
        return params

    def stop(self):
        """
        Sends the command to stop camera movement
        :return;
        """

        # Stop command is 1
        params = self.__getParams__(1)
        requests.get(self.url, params=params)

    def left(self):
        """
        Sends the command to turn the camera left
        :return;
        """

        # Left is command number 6
        params = self.__getParams__(6)
        requests.get(self.url, params=params)

    def right(self):
        """
        Sends the command to turn the camera right
        :return:
        """
        # Right command is 4
        params = self.__getParams__(4)
        requests.get(self.url, params=params)