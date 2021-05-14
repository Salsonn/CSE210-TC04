

import random

list = {
    1: ['A ♣', 'A ♥', 'A ♦', 'A ♠'],
    2: ['2 ♣', '2 ♥', '2 ♦', '2 ♠'],
    3: ['3 ♣', '3 ♥', '3 ♦', '3 ♠'],
    4: ['4 ♣', '4 ♥', '4 ♦', '4 ♠'],
    5: ['5 ♣', '5 ♥', '5 ♦', '5 ♠'],
    6: ['6 ♣', '6 ♥', '6 ♦', '6 ♠'],
    7: ['7 ♣', '7 ♥', '7 ♦', '7 ♠'],
    8: ['8 ♣', '8 ♥', '8 ♦', '8 ♠'],
    9: ['9 ♣', '9 ♥', '9 ♦', '9 ♠'],
    10: ['10 ♣', '10 ♥', '10 ♦', '10 ♠'],
    11: ['J ♣', 'J ♥', 'J ♦', 'J ♠'],
    12: ['Q ♣', 'Q ♥', 'Q ♦', 'Q ♠'],
    13: ['K ♣', 'K ♥', 'K ♦', 'K ♠']
}

class Dealer:

    global list

    def __init__(self):
        self.cards = list
        self.random_card()
        self.score = 0

    def random_card(self):

        # Chooses a random card from self.cards
        self.given_card = random.choice(list[random.randint(1, 13)])

        # Finds the value of the found card
        cards_value = self.card_value(self.given_card)

        # Removes selected card from the deck
        self.remove_card(self.given_card)

        print(self.given_card)
        # If this feat. is somehow attained, this will only trigger
        # If the player gets all 52 cards correct somehow
        if self.cards == []:
            # Returns a string if all cards correctly guessed
            return 'You Win!'
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

Dealer()