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

    def __init__(self, url, user, password, short_name):
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
        self.short_name = short_name

        # Since the counter is returning the actual preset value it is 1 indexed
        self.preset_counter = 1

        # Max number of presets
        self.__num_presets = 8

        # Check that URL and credentials are working
        params = {"user":self.user, "pwd":self.password}
        request = requests.get(self.url + self.check_user_resource, params=params)

        self.__check_status__(request)

    def get_short_name(self):
        """
        Gets the short name for the camera
        :return String:
        """
        return self.short_name

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

    def command(self, command_num):
        """
        Generic method to run a command, should generally only be used by other methods
        :param command_num:
        """

        params = self.__get_params__(command_num)
        request = requests.get(self.control_url, params=params)

        self.__check_status__(request)

    def stop(self):
        """
        Sends the command to stop camera movement
        :return;
        """

        # Stop command is 1
        self.command(1)


    def left(self):
        """
        Sends the command to turn the camera left
        :return;
        """

        # Left is command number 6
        self.command(6)

    def right(self):
        """
        Sends the command to turn the camera right
        :return:
        """
        # Right command is 4
        self.command(4)

    def up(self):
        """
        Sends the command to turn the camera up
        :return:
        """
        # Up command is 0
        self.command(0)

    def down(self):
        """
        Sends the command to turn the camera down
        :return:
        """
        # Down command is 2
        self.command(2)

    def up_right(self):
        """
        Sends the command to turn the camera up and to the right
        :return:
        """
        self.command(90)

    def down_right(self):
        """
        Sends the command to turn the camera down and to the right
        :return:
        """
        self.command(92)

    def down_left(self):
        """
        Sends the command to turn the camera down and to the right
        :return:
        """
        self.command(93)

    def up_left(self):
        """
        Sends the command to turn the camera down and to the right
        :return:
        """
        self.command(91)

    def center(self):
        """
        Sends the command to center the camera
        :return:
        """
        self.command(25)

    def ir_on(self):
        """
        Sends the command to turn on IR
        :return:
        """
        self.command(95)

    def ir_off(self):
        """
        Sends the command to turn off IR
        :return:
        """
        self.command(94)

    def vert_patrol(self):
        """
        Sends the command to do a vertical patrol
        :return:
        """
        self.command(26)

    def stop_vert_patrol(self):
        """
        Sends the command to stop doing the vertical patrol
        :return:
        """
        self.command(27)

    def horiz_patrol(self):
        """
        Sends the command to do a horizontal patrol
        :return:
        """
        self.command(28)

    def stop_horiz_patrol(self):
        """
        Sends the command to stop doing a horizontal patrol
        :return:
        """
        self.command(29)

    def set_preset(self, preset_num):
        """
        Sends the command to set a preset.
        Each of the eight presets has a different number, so this function maps 1-8 to the correct command number
        :param preset_num:
        :return:
        """

        # Check that preset number is in range
        if int(preset_num) < 1 or int(preset_num) > 8:
            raise ValueError('Preset number not in valid range (1-8')

        # Dictionary to map preset number to command number
        preset_commands = {"1":"30", "2":"32", "3":"34", "4":"36", "5":"38", "6":"40", "7":"42", "8":"44"}

        self.command(preset_commands[str(preset_num)])

    def go_preset(self, preset_num):
        """
        Sends the command to change to a preset.
        Each of the eight presets has a different number, so this function maps 1-8 to the correct command number
        :param preset_num:
        :return:
        """

        # Check that preset number is in range
        if int(preset_num) < 1 or int(preset_num) > self.__num_presets:
            raise ValueError('Preset number not in valid range (1-8')

        # Dictionary to map preset number to command number
        preset_commands = {"1":"31", "2":"33", "3":"35", "4":"37", "5":"39", "6":"41", "7":"43", "8":"45"}

        self.command(preset_commands[str(preset_num)])

    def get_pic_url(self):
        """
        Returns the location of a snapshot image
        :return: String
        """
        return self.url + "/snapshot.cgi?user=" + self.user + "&pwd=" + self.password

    def get_stream_url(self):
        """
        Returns the image stream's URL. This camera returns it as a constantly updating image.
        :return:
        """
        return self.url + "/videostream.cgi?user=" + self.user + "&pwd=" + self.password

    def get_num_presets(self):
        """
        Returns the number of presets
        :return: Integer
        """
        return self.__num_presets

    def __iter__(self):
        """
        Allows the camera's current preset number to be returned via an iterator
        :return:
        """
        return self

    def next(self):
        """
        Returns the next preset number to iterate on
        :return: Integer
        """
        # Check that the current preset is less than the max presets
        if self.preset_counter < self.__num_presets - 1:
            self.preset_counter += 1
            return self.preset_counter - 1
        else: # Reset back to 1 (the first preset
            self.preset_counter = 1
            return self.preset_counter