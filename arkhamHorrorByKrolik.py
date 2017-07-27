from game import Game
from player import Player

PLAYERS = [Player("Joanna", True), Player("Dawid"), Player("Carrie"), Player("Jonathan")]
game = Game(PLAYERS)

game.start_game()
