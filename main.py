from logic import lets_play_blackjack
from util import build_deck, suits, values, number_of_decks, valid_user_option, get_valid_input

deck = build_deck(suits, values, number_of_decks)

while True:
    if len(deck) < 52:
        print("Reshuffling the shoe...")
        deck = build_deck(suits, values, number_of_decks)

    game_start = get_valid_input('Would you like play a new hand of BlackJack?', valid_user_option)
    if game_start == 'y':
        lets_play_blackjack(deck)
    else:
        break
