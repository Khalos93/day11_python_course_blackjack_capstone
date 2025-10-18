from logic import lets_play_blackjack
from util import build_deck, suits, values, number_of_decks, valid_user_option, get_valid_input

game_is_on = True
deck = build_deck(suits, values, number_of_decks)

while game_is_on:
    game_start = get_valid_input('Would you like play a new hand of BlackJack?', valid_user_option)
    if game_start == 'y':
        lets_play_blackjack(deck)
    else:
        game_is_on = False
