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

    def __check_status__(self, request):
        """
        Checks to see if the return status from the camera is OK
        :param request:
        :return:
        """

        if (request.status_code != requests.codes.ok):
            request.raise_for_status()

    def stop(self):
        """
        Sends the command to stop camera movement
        :return;
        """

        # Stop command is 1
        params = self.__get_params__(1)
        request = requests.get(self.url, params=params)

        self.__check_status__(request)


    def left(self):
        """
        Sends the command to turn the camera left
        :return;
        """

        # Left is command number 6
        params = self.__get_params__(6)
        request = requests.get(self.url, params=params)

        self.__check_status__(request)

    def right(self):
        """
        Sends the command to turn the camera right
        :return:
        """
        # Right command is 4
        params = self.__get_params__(4)
        request = requests.get(self.url, params=params)

        self.__check_status__(request)