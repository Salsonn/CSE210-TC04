from game.dealer import Dealer

class Director:
    # The Director behaves as the person overseeing the game, commands the dealer,
    # gets user input, keeps score, and determines when the game is over.
    def __init__(self):
        # Starts the Dealer and prepares the game.
        '''Setting up the appropriate variables and initializing dealer'''
        self.dealer = Dealer()
        '''Boolean controls whether gameplay should continue at the end of a round'''
        self.keep_playing = True

    def get_input(self):
        '''Display the starting card for each deal. 
        Then receive input from user'''
        self.display_chosen()
        self.player_guess = input('Is the next card higher or lower [H/L]: ')
        while not (self.player_guess == 'h' or self.player_guess =='l'):
                self.player_guess = input("\n\033[31mInvalid Input, please type 'h' or 'l'\033[m\nIs the next card higher or lower [H/L]: ")

    def do_updates(self):
        '''Update the score and quit if score is 0'''
        if self.first_card_value <= self.second_card_value:
            if self.player_guess == "h":
                self.dealer.score += 100
                print("\033[33m    Good guess!\033[m")
            else:
                self.dealer.score -= 75
                print("\033[31m    Uh oh!\033[m")
        elif self.first_card_value >= self.second_card_value:
            if self.player_guess == "l":
                self.dealer.score += 100
                print("\033[33m    Good guess!\033[m")
            else:
                self.dealer.score -= 75
                print("\033[31m    Uh oh!\033[m")

    def do_outputs(self):
        '''Displays the next unknown card
        and prompt the user if they want to 
        keep plaing the game'''
        print(f"Your score is now \033[34m{self.dealer.score} points.\033[m")

        if self.dealer.score > 0:
            play_again = input(f'Would you like to keep playing? [Y/N] ')
            while not (play_again == 'n' or play_again =='y'):
                play_again = input("\033[31mInvalid Input, please type 'y' or 'n'\033[m\nWould you like to keep playing? [Y/N] ")
            if play_again == 'n':
                self.keep_playing = False
        else:
            print("Game Over!")
            quit()

    def start_game(self):
        '''Game loop'''
        print("\n\n\033[34mWelcome to HiLo!\033[m")
        while self.keep_playing:
            self.first_card, self.first_card_value = self.dealer.random_card()
            self.get_input()
            self.second_card, self.second_card_value = self.dealer.random_card()
            self.display_future()
            self.do_updates()
            self.do_outputs()
        print(f"\nThank you for playing!\nYour final score is \033[34m{self.dealer.score} points.\033[m")

    def display_chosen(self):
        '''Displays the first card'''
        print(f'\n\nThe first card card is: {self.first_card}')

    def display_future(self):
        '''Reveals the next card'''
        print(f'The card is: {self.second_card}\n\n')
