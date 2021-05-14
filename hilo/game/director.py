from game.dealer import Dealer

class Director:

    def __init__(self):
        '''Setting up the appropriate variables'''
        self.keep_playing = True
        self.chosen_card = self.dealer.random_card()
        self.future_card = self.chosen_card
        self.dealer = Dealer()

    def get_input(self):
        '''Display the starting card for each deal. 
        Then receive input from user'''
        self.display_chosen()
        self.player_guess = input('High or Low [h/l]: ')

    def do_updates(self):
        '''Update the score and quit if score is 0'''
        if self.dealer.check_guess(self.player_guess) == True:
            self.dealer.score += 100
        elif self.dealer.check_guess(self.player_guess) == False:
            self.dealer.score -= 75
        elif self.dealer.score == 0:
            quit()

    def do_outputs(self):
        '''Displays the next unknown card
        and prompt the user if they want to 
        keep plaing the game'''
        self.display_future()

        if self.dealer.score > 0:
            play_agian = input(f'Would you like to play again? [y/n]')
        
        if play_agian == 'y':
            self.keep_playing = True

        else:
            self.keep_playing = False

    def start_game(self):
        '''Game loop'''
        while self.keep_playing:
            self.get_input()
            self.do_updates()
            self.do_outputs()

    def display_chosen(self):
        '''Displays the chosen card'''
        print(f'the chosen card is: {self.chosen_card}')

    def display_future(self):
        '''Reveals the next card'''
        print(f'the future card is: {self.future_card}')
        

Director()