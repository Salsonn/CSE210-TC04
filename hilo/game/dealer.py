

import random

list = {
    1: ['A \033[47m\033[30m♣\033[m', 'A \033[31m\033[47m♥\033[m', 'A \033[31m\033[47m♦\033[m', 'A \033[47m\033[30m♠\033[m'],
    2: ['2 \033[47m\033[30m♣\033[m', '2 \033[31m\033[47m♥\033[m', '2 \033[31m\033[47m♦\033[m', '2 \033[47m\033[30m♠\033[m'],
    3: ['3 \033[47m\033[30m♣\033[m', '3 \033[31m\033[47m♥\033[m', '3 \033[31m\033[47m♦\033[m', '3 \033[47m\033[30m♠\033[m'],
    4: ['4 \033[47m\033[30m♣\033[m', '4 \033[31m\033[47m♥\033[m', '4 \033[31m\033[47m♦\033[m', '4 \033[47m\033[30m♠\033[m'],
    5: ['5 \033[47m\033[30m♣\033[m', '5 \033[31m\033[47m♥\033[m', '5 \033[31m\033[47m♦\033[m', '5 \033[47m\033[30m♠\033[m'],
    6: ['6 \033[47m\033[30m♣\033[m', '6 \033[31m\033[47m♥\033[m', '6 \033[31m\033[47m♦\033[m', '6 \033[47m\033[30m♠\033[m'],
    7: ['7 \033[47m\033[30m♣\033[m', '7 \033[31m\033[47m♥\033[m', '7 \033[31m\033[47m♦\033[m', '7 \033[47m\033[30m♠\033[m'],
    8: ['8 \033[47m\033[30m♣\033[m', '8 \033[31m\033[47m♥\033[m', '8 \033[31m\033[47m♦\033[m', '8 \033[47m\033[30m♠\033[m'],
    9: ['9 \033[47m\033[30m♣\033[m', '9 \033[31m\033[47m♥\033[m', '9 \033[31m\033[47m♦\033[m', '9 \033[47m\033[30m♠\033[m'],
    9: ['10 \033[47m\033[30m♣\033[m', '10 \033[31m\033[47m♥\033[m', '10 \033[31m\033[47m♦\033[m', '10 \033[47m\033[30m♠\033[m'],
    11: ['J \033[47m\033[30m♣\033[m', 'J \033[31m\033[47m♥\033[m', 'J \033[31m\033[47m♦\033[m', 'J \033[47m\033[30m♠\033[m'],
    12: ['Q \033[47m\033[30m♣\033[m', 'Q \033[31m\033[47m♥\033[m', 'Q \033[31m\033[47m♦\033[m', 'Q \033[47m\033[30m♠\033[m'],
    13: ['K \033[47m\033[30m♣\033[m', 'K \033[31m\033[47m♥\033[m', 'K \033[31m\033[47m♦\033[m', 'K \033[47m\033[30m♠\033[m']
}

class Dealer:

    global list

    def __init__(self):
        # Container for card data and appearance
        self.cards = list
        # Sets the starting score for the game
        self.score = 300

    def random_card(self):

        # Chooses a random card from self.cards
        self.given_card = random.choice(list[random.randint(1, 13)])

        # Finds the value of the found card
        cards_value = self.card_value(self.given_card)

        # Removes selected card from the deck
        self.remove_card(self.given_card)

        # If this feat. is somehow attained, this will only trigger
        # If the player gets all 52 cards correct somehow
        if self.cards == []:
            # Returns a string if all cards correctly guessed
            victory=['No more cards left. You Win!','You won! Wait, how did you do that?','I bet you feel prety clever huh? There are no more cards.']
            print(random.choice(victory))
            quit()
        else:
            # Otherwise, it just returns the card and its value
            return self.given_card, cards_value
    
    def remove_card(self, given_card):
        # Iterates through each value in the list
        for i in list:

            # This checks if the card was found
            if given_card in list[i]:

                # If the card was found, it grabs its index value and pops it off the list
                index_value = list[i].index(given_card)
                list[i].pop(index_value)

    def card_value(self, given_card):

        # Iterates through the list to find the given card
        for i in list:

            # Once the card is found, it finds the card value and returns it
            if given_card in list[i]:
                return i
