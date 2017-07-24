from textUserInterfaceUtils import TextUserInterfaceUtils as Utils

class Game:
    def __init__(self):
        self.__turns_passed = 0
        self.__turns_cap = 1000

    @property
    def turns_passed(self):
        return self.__turns_passed

    @turns_passed.setter
    def turns_passed(self, val):
        if val < self.__turns_cap and val > 0:
            self.__turns_passed = val
        else



    def start_game(self):
        print Utils.add_asterisk(6) + "Arkham Horror starts now!!!" + Utils.add_asterisk(6)

    def is_game_over(self):
        if self.turns_passed < self.turns_passed:
            return True

        return False

if __name__ == "__main__":
    print "ArkhamHorrow Game Kurwa!!!"