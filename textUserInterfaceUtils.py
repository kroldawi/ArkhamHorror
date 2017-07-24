class TextUserInterfaceUtils:

    @staticmethod
    def add_text(str, qty):
        """Generic method to build a text that consist of specified number of input string."""
        s = ""
        i = 0
        while i < qty:
            s += str
            i += 1

        return s

    @staticmethod
    def add_text_spaced(str, qty = 1):
        """Version of add_text but with spaces."""
        return TextUserInterfaceUtils.add_text(str + " ", qty)

    @staticmethod
    def add_asterisk(qty):
        """Generate string build of qty asterisks."""
        return TextUserInterfaceUtils.add_text("*", qty)

    @staticmethod
    def create_h1(str):
        s = TextUserInterfaceUtils.add_text_spaced(".", 3) + TextUserInterfaceUtils.add_text_spaced("*", 4)
        s += TextUserInterfaceUtils.add_text_spaced(str);
        s += TextUserInterfaceUtils.add_text_spaced("*", 4) + TextUserInterfaceUtils.add_text_spaced(".", 3)

        return s


if __name__ == "__main__":
    print "TextUserInterfactUtils dev test"

    #utils = TextUserInterfaceUtils()
    print TextUserInterfaceUtils.add_text("-", 10)
    print TextUserInterfaceUtils.add_asterisk(11)