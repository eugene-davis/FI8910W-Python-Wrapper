__author__ = 'Eugene Davis'

import requests

class FI8910W_wrapper:

    # User parameter to hand off to camera
    user = "";
    # Password parameter to hand off to camera
    password = ""
    # URL to camera
    url = ""

    # Constructor - sets the username and password
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password

    # Creates the parameters key-value array for URL
    def __genParams(self, command):
        params = {"user":self.user, "pwd":self.password, "command":command}
        return params

    # Stops camera movement
    def stop(self):
        # Stop command is 1
        params = self.__genParams(1)
        requests.get(self.url, params=params)

    # Moves the camera left
    def left(self):
        # Left is command number 6
        params = self.__genParams(6)
        requests.get(self.url, params=params)

    # Moves the camera right
    def right(self):
        # Left command is 4
        params = self.__genParams(4)
        requests.get(self.url, params=params)