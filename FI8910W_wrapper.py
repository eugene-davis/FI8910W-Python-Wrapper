__author__ = 'Eugene Davis'

import requests

class FI8910W_wrapper:

    # User parameter to hand off to camera
    user = "";
    # Password parameter to hand off to camera
    password = ""
    # URL to camera
    url = ""
    # Full control URL
    control_url = ""
    # Resource to check user
    check_user_resource = "/check_user2.cgi"
    # URL for control operations
    control_resource = "/decoder_control.cgi"

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
        self.control_url = self.url + self.control_resource

        # Check that URL and credentials are working
        params = {"user":self.user, "pwd":self.password}
        request = requests.get(self.url + self.check_user_resource, params=params)

        self.__check_status__(request)


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
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)


    def left(self):
        """
        Sends the command to turn the camera left
        :return;
        """

        # Left is command number 6
        params = self.__get_params__(6)
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)

    def right(self):
        """
        Sends the command to turn the camera right
        :return:
        """
        # Right command is 4
        params = self.__get_params__(4)
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)

    def up(self):
        """
        Sends the command to turn the camera up
        :return:
        """
        # Right command is 0
        params = self.__get_params__(0)
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)

    def down(self):
        """
        Sends the command to turn the camera down
        :return:
        """
        # Right command is 2
        params = self.__get_params__(2)
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)