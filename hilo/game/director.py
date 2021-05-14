from game.dealer import Dealer

class Director:
    # The Director behaves as the person overseeing the game, commands the dealer,
    # gets user input, keeps score, and determines when the game is over.
    def __init__(self):
<<<<<<< Updated upstream
        # Starts the Dealer and prepares the game.

        self.dealer = Dealer()
=======
        '''Setting up the appropriate variables and initializing dealer'''
        self.dealer = Dealer()
        self.keep_playing = True

    def get_input(self):
        '''Display the starting card for each deal. 
        Then receive input from user'''
        self.display_chosen()
        self.player_guess = input('High or Low [h/l]: ')

    def do_updates(self):
        '''Update the score and quit if score is 0'''
        '''if self.dealer.check_guess(self.player_guess) == True:
            self.dealer.score += 100
        elif self.dealer.check_guess(self.player_guess) == False:
            self.dealer.score -= 75'''
        # print(f"comparing card 1 ({self.first_card}")
        # print(f"value is: {self.dealer.card_value(self.first_card)}")
        # print(f"With card 2 ({self.second_card}")
        if self.dealer.card_value(self.first_card) < self.dealer.card_value(self.second_card):
            if self.player_guess == "h":
                self.dealer.score += 100
            else:
                self.dealer.score -= 75
        if self.dealer.card_value(self.first_card) > self.dealer.card_value(self.second_card):
            if self.player_guess == "l":
                self.dealer.score += 100
            else:
                self.dealer.score -= 75

    def do_outputs(self):
        '''Displays the next unknown card
        and prompt the user if they want to 
        keep plaing the game'''
        self.display_future()
        print("Your score is now " . self.dealer.score)

        if self.dealer.score > 0:
            play_again = input(f'Would you like to play again? [y/n]')
            if play_again == 'n':
                self.keep_playing = False
        else:
            print("Game Over!")
            quit()

    def start_game(self):
        '''Game loop'''
        while self.keep_playing:
            self.first_card = self.dealer.random_card()
            self.get_input()
            self.second_card = self.dealer.random_card()
            self.do_updates()
            self.do_outputs()

    def display_chosen(self):
        '''Displays the first card'''
        print(f'The first card card is: {self.first_card}')
        print("It's value is:")
        self.dealer.card_value(self.first_card)

    def display_future(self):
        '''Reveals the next card'''
        print(f'The card is: {self.second_card}')
>>>>>>> Stashed changes
