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

    def is_phase_over(self):
        return True

    def start_phase(self, players):
        print Utils.add_indent(2), Utils.create_h2(self.name, 30)

        while not self.is_phase_over():
            print "We have a bug here!!!"

if __name__ == "__main__":
    print "ArkhamHorrow Kurwa!!!"