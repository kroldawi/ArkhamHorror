from textUserInterfaceUtils import TextUserInterfaceUtils as Utils


class Phase(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        pass

    def execute_phase(self, player):
        pass

    def is_phase_over(self, players):
        return players.has_all_players_played()

    def start_phase(self, players):
        print Utils.add_indent(2), Utils.create_h2(self.name, 30)

        while not self.is_phase_over(players):
            player = players.get_next_player()
            self.execute_phase(player)

        players.pass_first_player_token()

if __name__ == "__main__":
    print "ArkhamHorrow Kurwa!!!"