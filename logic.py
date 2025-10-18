import random

from util import (card_tens, card_ace, calculate_score, turn_has_blackjack,
                  winner_check, get_valid_input, valid_user_option)


def lets_play_blackjack(deck):

    while True:
        user_cards = []
        dealer_cards = []

        user_cards.append(deck.pop())
        dealer_cards.append(deck.pop())
        user_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

        dealer_score = calculate_score(dealer_cards)
        user_score = calculate_score(user_cards)

        print(f"Your cards are {user_cards} for a total score of: {user_score}")
        print(f"Dealer cards are {dealer_cards[0]}")

        dealer_has_blackjack = turn_has_blackjack(dealer_score)
        user_has_blackjack = turn_has_blackjack(user_score)

        if dealer_has_blackjack and not user_has_blackjack:
            print("Dealer has BlackJack")
            return
        elif dealer_has_blackjack and user_has_blackjack:
            print("Both you and the dealer hit Blackjack..! This round is a push..!")
            return
        elif not dealer_has_blackjack and user_has_blackjack:
            print("Congratulation you hit BlackJack")
            return

        while user_score < 21:
            one_more_card = get_valid_input("Would you like another card? Type 'Y' or 'N'", valid_user_option)
            if one_more_card == 'y':
                user_cards.append(deck.pop())
                user_score = calculate_score(user_cards)

                if user_score > 21:
                    print(f"You busted! Your cards are {user_cards} for a total score of: {user_score}")
                    break
                else:
                    print(f"Your cards are {user_cards} for a total score of: {user_score}")

            else:
                print(f"Your final cards are {user_cards} for a total score of: {user_score}")
                break

        while dealer_score < 17:
            dealer_cards.append(deck.pop())
            dealer_score = calculate_score(dealer_cards)

        final_result = winner_check(user_score, dealer_score, user_cards, dealer_cards)
        print(final_result)
        break
