from player import Player


class Players(object):

    def __init__(self, players=None):
        self.__players = players
        if self.__players is None:
            self.__players = [Player("Forever Alone Skurwiel", True)]

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, val):
        pass

    def current_player

    def pass_first_player_token(self):
        first_player = self.first_player()
        new_first_player = divmod(first_player + 1, len(self.__players))[1]

        self.__players[first_player].pass_first_player_token()
        self.__players[new_first_player].receive_first_player_token()

    def first_player(self):
        for p in self.__players:
            if p.has_first_player_token():
                return self.__players.index(p)

        raise ValueError("At least one player should have first player token.")