import random
from colorama import Fore, Style, init
init()

print(Fore.YELLOW + "\nWELCOME TO THE GAME BESTIEEE!!!")
print("\nGame Rules:\n*no blushing*\n*no giggling*\n*no smiling*"+ Style.RESET_ALL)

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

def show_hand(hand, who="player", all_cards = True):
    print(f"\n{who}'s hand:")
    if who == "dealer" and all_cards == False:
        print(hand.cards[0], ", <hidden card>")
    else:
        for card in hand.cards:
            print(card)
        print("\nvalue:", hand.value)

def player_hit(hand):
    hand.add_card(deck.deal())
    print("current value:", hand.value)

    if hand.value > 21:
        print(Fore.RED + "Player busts...😔😔😔😔"+ Style.RESET_ALL)
        print(Fore.CYAN + "DEALER WINSSSS"+ Style.RESET_ALL)

def dealer_hit(hand):
    while hand.value < 17:
        hand.add_card(deck.deal())
        print("current value:", hand.value)

game_on = True

while game_on: 

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_hand(player_hand,"player")
    show_hand(dealer_hand, "dealer", False)  

    while player_hand.value < 21:
        player_input = input("\nDo you wanna hit? \n enter y/n:").lower()
        if player_input == "y":
            player_hit(player_hand)
            print()
            show_hand(player_hand)
        else:
            print("player has decided to stay")
            break

    print("\nit is now the dealer's turn")
    
    if player_hand.value <= 21:
        dealer_hit(dealer_hand)
        print()
        show_hand(dealer_hand, "dealer")

        if dealer_hand.value > 21:
            print(Fore.MAGENTA + "Dealer BUSTS! Player wins 🎉🎉🎉🎉🎉"+ Style.RESET_ALL)
        elif dealer_hand.value > player_hand.value:
            print(Fore.GREEN + "Dealer wins 😔😔😔😔😔😔"+ Style.RESET_ALL)
        elif dealer_hand.value < player_hand.value:
            print(Fore.MAGENTA+ "Player wins 🎉🎉🎉🎉🎉🎉"+ Style.RESET_ALL)
        else:
            print(Fore.LIGHTMAGENTA_EX + "It's a tie! 🤝🤝🤝🤝🤝🤝🤝 *pretty sure dealer cheated-*"+ Style.RESET_ALL)
    
    player = input("\ndo you wanna play another round? \n enter y/n:").lower()
    if player == "n":
        game_on = False
    else:
        continue

