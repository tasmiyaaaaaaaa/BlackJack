import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    
    def __str__(self):
        every_card = ''
        for card in self.deck:
            every_card+= '\n' + str(card)
        return f'THE DECK HAS: {every_card}'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card    

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value+= values[card.rank]
        if card.rank == "Ace" :
            self.aces+=1
        self.handle_ace()
        
    def handle_ace(self):
        while self.aces > 0 and self.value > 21:  
            self.value-= 10
            self.aces-= 1     

deck = Deck()
deck.shuffle()

player = Hand()
player.add_card(deck.deal())
player.add_card(deck.deal())

dealer = Hand()
dealer.add_card(deck.deal())
dealer.add_card(deck.deal())


