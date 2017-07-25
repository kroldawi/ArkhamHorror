from textUserInterfaceUtils import TextUserInterfaceUtils as Utils


class Player(object):

    def __init__(self, name, first_player_token = False):
        self.__name = name
        self.__first_player_token = first_player_token

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        pass

    def has_first_player_token(self):
        return self.__first_player_token

    def pass_first_player_token(self):
        self.__first_player_token = False

    def receive_first_player_token(self):
        self.__first_player_token = True
