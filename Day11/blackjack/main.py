from random import choice
from art import logo

def hit_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    # if card == 1 or card == 11:
    #     cards.remove(1)
    #     cards.remove(11)
    # else:
    cards.remove(card)
    return card


def hit_2_first_cards():
    hit_cards = []
    for i in range(0, 2):
        hit_cards.append(hit_card())
    return hit_cards


def should_hit_more_card(card_mark):
    if card_mark < 17:
        return True
    else:
        return False


def check_result(computer_mark, player_mark):
    if player_mark > 21 or player_mark < 17:
        return "LOSE"
    elif computer_mark > 21 or computer_mark < 17:
        return "WON"
    elif player_mark > computer_mark:
        return "WON"
    elif player_mark < computer_mark:
        return "LOSE"
    else:
        return "DRAWN"


computer_cards = hit_2_first_cards()
player_cards = hit_2_first_cards()


def play_blackjack():
    print(f"The first card of computer is {computer_cards[0]}.")
    print(f"Your cards are: {player_cards}.")
    if sum(player_cards) == 21 and len(player_cards) == 2:
        print(f"Your cards are {player_cards}. You WON")
    want_to_hit = input("Do you want to hit a card? Type 'y' to hit, or type 'n' to pass. ")
    if want_to_hit == 'y':
        player_cards.append(hit_card())
        play_blackjack()
    elif want_to_hit == 'n':
        while should_hit_more_card(sum(computer_cards)):
            computer_cards.append(hit_card())
        print(f"Computer's cards are {computer_cards}")
        print(f"Your cards are {player_cards}")
        print(f"You {check_result(sum(computer_cards), sum(player_cards))}")


print(logo)
play_blackjack()
