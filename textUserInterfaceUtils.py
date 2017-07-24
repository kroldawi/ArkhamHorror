class TextUserInterfaceUtils:

    @staticmethod
    def add_text(str, qty):
        """Generic method to build a text that consist of specified number of input string."""
        s = ""
        while len(s) < qty:
            s += str

        return s

    @staticmethod
    def add_asterisk(qty):
        """Generate string build of qty asterisks."""
        return TextUserInterfaceUtils.add_text("*", qty)


if __name__ == "__main__":
    print "TextUserInterfactUtils dev test"

    #utils = TextUserInterfaceUtils()
    print TextUserInterfaceUtils.add_text("-", 10)
    print TextUserInterfaceUtils.add_asterisk(11)