from textUserInterfaceUtils import TextUserInterfaceUtils as Utils
from phase import Phase


class UpkeepPhase(Phase):
    def execute_phase(self, player):
        print Utils.add_indent(4) + "Now it's " + player.name + "'s turn"