from game.dealer import Dealer

class Director:
    # The Director behaves as the person overseeing the game, commands the dealer,
    # gets user input, keeps score, and determines when the game is over.
    def __init__(self):
        # Starts the Dealer and prepares the game.

        self.dealer = Dealer()
