import random

suits = ['♠', '♥', '♦', '♣']  # Using Unicode symbols
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
number_of_decks = 6
card_tens = ('J', 'Q', "K")
card_ace = "A"
valid_user_option = ('y', 'n')


def build_deck(seeds: [str], card_values: [str], num_decks: int) -> [str]:
    single_deck = [(card_value, seed) for seed in seeds for card_value in card_values]
    game_deck = single_deck * num_decks
    random.shuffle(game_deck)
    return game_deck


def calculate_score(turn_cards: [str]) -> int:
    turn_score = []

    for card in turn_cards:
        rank = card[0]

        if rank in card_tens:
            turn_score.append(10)
        elif rank == card_ace:
            turn_score.append(11)
        else:
            turn_score.append(int(rank))

        total = sum(turn_score)

        while total > 21 and 11 in turn_score:
            ace_index = turn_score.index(11)
            turn_score[ace_index] = 1
            total = sum(turn_score)

    return total


def turn_has_blackjack(turn_score: int) -> bool:
    if turn_score == 21:
        return True
    else:
        return False


def get_valid_input(sentence: str, valid_options: tuple[str]) -> str:
    while True:

        user_response = input(sentence).lower()
        if user_response in valid_options:
            return user_response
        print(f"Invalid input..! Please try again.")


def winner_check(player_point: int, opponent_points: int, player_cards: [str], opponent_cards: [str]) -> str:
    if player_point > 21 and opponent_points > 21:
        return (f"You both BUST..!\nYour cards: {player_cards} with a total score of {player_point}\n"
                f"Dealer cards: {opponent_cards} with a total score of {opponent_points}")
    elif player_point > 21 >= opponent_points:
        return (
            f"You BUST..! Dealer win this hand..!\nYour cards: {player_cards} with a total score of {player_point}\n"
            f"Dealer cards: {opponent_cards} with a total score of {opponent_points}")
    elif player_point == 21 and opponent_points == 21:
        return (
            f"Both you and the Dealer hit 21..! This hand end with a TIE\nYour cards: {player_cards} with a total score of {player_point}\n"
            f"Dealer cards: {opponent_cards} with a total score of {opponent_points}")
    elif 21 >= player_point > opponent_points:
        return (f"WINNER WINNER CHICKEN DINNER..!\nYour cards: {player_cards} with a total score of {player_point}\n"
                f"Dealer cards: {opponent_cards} with a total score of {opponent_points}")
    elif 21 >= opponent_points > player_point:
        return (f"Dealer wins this hand.\nYour cards: {player_cards} with {player_point}\n"
                f"Dealer cards: {opponent_cards} with {opponent_points}")
    elif opponent_points > 21 >= player_point:
        return (f"WINNER WINNER CHICKEN DINNER..! Dealer busted!\nYour cards: {player_cards} with a total score of {player_point}\n"
                f"Dealer cards: {opponent_cards} with a total score of {opponent_points}")
    elif opponent_points < 21 and opponent_points == player_point:
        return (
            f"Both you and the Dealer hold the same points..! This hand end with a TIE\nYour cards: {player_cards} "
            f"with a total score of {player_point}\nDealer cards: {opponent_cards} with a total score of {opponent_points}")
    else:
        # 👇 final catch-all fallback (should rarely trigger)
        return (f"Round ended with no clear winner (possible logic gap)\n"
                f"Your cards: {player_cards} ({player_point}) | "
                f"Dealer cards: {opponent_cards} ({opponent_points})")
