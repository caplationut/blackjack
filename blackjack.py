import random
import os

# Global constants
SUITS = ['♠', '♣', '♦', '♥']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return self.rank + self.suit

# Deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.total += CARD_VALUES[card.rank]
        if card.rank == 'A':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.total > 21 and self.aces > 0:
            self.total -= 10
            self.aces -= 1
    
    def is_busted(self):
        return self.total > 21
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.total == 21
    
    def __str__(self):
        return ', '.join([str(card) for card in self.cards]) + ' (' + str(self.total) + ')'

# Main game logic
def blackjack_game():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    
    print("Welcome to Blackjack!")
    
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    
    # Create player's and dealer's hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal initial cards
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    # Player's turn
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Player's Hand:", player_hand)
        print("Dealer's Hand:", dealer_hand.cards[0])
        
        if player_hand.is_blackjack():
            print("Blackjack! You win!")
            return
        
        if player_hand.is_busted():
            print("Busted! You lose.")
            return
        
        choice = input("Do you want to hit or stand? (h/s): ")
        
        if choice.lower() == 'h':
            player_hand.add_card(deck.deal_card())
            player_hand.adjust_for_ace()
        elif choice.lower() == 's':
            break

     # Dealer's turn
    while dealer_hand.total < 17:
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.adjust_for_ace()

    # Determine the winner
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Player's Hand:", player_hand)
    print("Dealer's Hand:", dealer_hand)

    if dealer_hand.is_busted():
        print("Dealer busts! You win!")
    elif dealer_hand.total > player_hand.total:
        print("Dealer wins!")
    elif dealer_hand.total < player_hand.total:
        print("You win!")
    else:
        print("It's a tie!")

# Start the game
while True:
    blackjack_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
