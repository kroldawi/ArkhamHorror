from textUserInterfaceUtils import TextUserInterfaceUtils as Utils
from phase import Phase
from players import Players


class Game(object):

    def __init__(self, players=None):
        self.__turns_passed = 0
        self.__turns_cap = 1000
        self.__phases = [Phase("Upkeep Phase"), Phase("Movement Phase"), Phase("Arkham Encounter Phase"), Phase("Otherworld Encounter Phase"), Phase("Mythos Phase")]

        self.__players = players
        if self.__players is None:
            self.__players = Players()

    @property
    def turns_passed(self):
        return self.__turns_passed

    @turns_passed.setter
    def turns_passed(self, val):
        if val < 0:
            raise ValueError("Invalid turns_passed parameter value.")

        self.__turns_passed = val

    @property
    def turns_cap(self):
        return self.__turns_cap

    @turns_cap.setter
    def turns_cap(self, val):
        pass

    def is_game_over(self):
        if self.turns_passed < self.turns_cap:
            return False

        return True

    def start_game(self):
        print Utils.create_h1("Arkham Horror starts now!!!")

        while not self.is_game_over():
            print "Turn: ", self.turns_passed, " out of ", self.turns_cap
            for p in self.__phases:
                p.start_phase()

            self.turns_passed += 1


if __name__ == "__main__":
    print "ArkhamHorrow Game Kurwa!!!"

    game = Game()


