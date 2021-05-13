import random

# Code for the dealer class goes here

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
        self.given_card = random.choice(list[random.randint(1, 4)])
        print(self.given_card)
        return self.given_card

Dealer()