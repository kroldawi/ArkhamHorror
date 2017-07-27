from player import Player


class Players(object):

    def __init__(self, players=None):
        self.__players = players
        if self.__players is None:
            self.__players = [Player("Forever Alone Skurwiel", True)]

        self.__current_player_id = None

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, val):
        pass

    def next_player(self, player_id):
        return 0 if player_id + 1 == len(self.__players) else player_id + 1

    def get_next_player(self):
        if self.__current_player_id is None:
            self.__current_player_id = self.__players.index(self.first_player())
        else:
            self.__current_player_id = self.next_player(self.__current_player_id)

        return self.__players[self.__current_player_id]

    def has_all_players_played(self):
        if self.__current_player_id is None:
            return False

        next_player = self.__players[self.next_player(self.__current_player_id)]
        return next_player.has_first_player_token()

    def pass_first_player_token(self):
        first_player = self.first_player()
        first_player_id = self.__players.index(first_player)
        new_first_player = self.__players[self.next_player(first_player_id)]

        first_player.pass_first_player_token()
        new_first_player.receive_first_player_token()

        self.__current_player_id = None

    def first_player(self):
        for p in self.__players:
            if p.has_first_player_token():
                return p

        raise ValueError("At least one player should have first player token.")