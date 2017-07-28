from textUserInterfaceUtils import TextUserInterfaceUtils as Utils


class Character(object):

    def __init__(self, name, profession, max_stamina, max_sanity, focus):
        self.__name = name
        self.__profession = profession
        self.__max_stamina = max_stamina
        self.__max_sanity = max_sanity
        self.__focus = focus
        self.__stamina = max_stamina
        self.__sanity = max_sanity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        pass

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, val):
        pass

    @property
    def focus(self):
        return self.__focus

    @focus.setter
    def focus(self, val):
        pass

    @property
    def max_stamina(self):
        return self.__max_stamina

    @max_stamina.setter
    def max_stamina(self, val):
        self.__max_stamina = 0 if val < 0 else val

    @property
    def max_sanity(self):
        return self.__max_sanity

    @max_sanity.setter
    def max_sanity(self, val):
        self.__max_sanity = 0 if val < 0 else val

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, val):
        self.__stamina = 0 if val < 0 else val

    @property
    def sanity(self):
        return self.__sanity

    @sanity.setter
    def sanity(self, val):
        self.__sanity = 0 if val < 0 else val

