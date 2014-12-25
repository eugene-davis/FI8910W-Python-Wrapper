__author__ = 'Eugene Davis'

class FI8910W_wrapper:

    # User parameter to hand off to camera
    user = "";
    # Password parameter to hand off to camera
    password = ""

    # Constructor - sets the username and password
    def __init(self, user, password):
        self.user = user
        self.password = password

    # Creates the parameters key-value array for URL
    def __genParams(self, command):
        params = {"user":self.user, "pwd":self.password, "command":command}
        return params