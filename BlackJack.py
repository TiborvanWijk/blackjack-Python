from random import choice


def scorecalulator(first_card):
    player_score = 0
    if first_card == 11:
        player_score += 10
        return player_score
    elif first_card == 12:
        player_score += 10
        return player_score
    elif first_card == 13:
        player_score += 10
        return player_score
    elif first_card == 14:
        ace = input("You got an ace would you like 11 or 1 point?:")
        if ace == "11":
            player_score += 11
            return player_score
        elif ace == "1":
            player_score += 1
            return player_score
    else:
        player_score += first_card
        return player_score


def scorecalulatordealer(first_card):
    player_score = 0
    if first_card == 11:
        player_score += 10
        return player_score
    elif first_card == 12:
        player_score += 10
        return player_score
    elif first_card == 13:
        player_score += 10
        return player_score
    elif first_card == 14:
        if player_score < 12:
            player_score += 11
        else:
            player_score += 1
        return player_score
    else:
        player_score += first_card
        return player_score


def cardtype(first_card, card_type):
    if first_card == 11:
        print("Queen", card_type)
    elif first_card == 12:
        print("King", card_type)
    elif first_card == 13:
        print("Jack", card_type)
    elif first_card == 14:
        print("Ace", card_type)
    else:
        print(first_card, card_type)
    return '----------------------'


def hit_stand(player_score, dealer_score):
    while True:
        if player_score == 21:
            print("----------\nYou win!!!\n----------")
            break
        if float(player_score) > 21:
            print("-----------\nYou Lose!!!\n-----------")
            break
        hit = input("Do you want to hit or stand?: ")
        if hit == "hit":
            new_card = choice(card_value)
            if new_card == 11:
                player_score += 10
                new_card = "Queen"
            elif new_card == 12:
                player_score += 10
                new_card = "King"
            elif new_card == 13:
                player_score += 10
                new_card = "Jack"
            elif new_card == 14:
                ace = input("You got an ace would you like 11 or 1 point?:")
                new_card = "Ace"
                if ace == "11":
                    player_score += 11
                elif ace == "1":
                    player_score += 1
            else:
                player_score += new_card
            print("-----------------------------\nYour new card is:", new_card, choice(card_type),
                  "\n-----------------------------")
            print("Your score is:", player_score)
            print("Dealer's score is:", dealer_score)
        if hit == "stand":
            dealer_new_card = choice(card_value)
            if dealer_new_card == 11:
                dealer_new_card = "Queen"
                dealer_score += 10
            elif dealer_new_card == 12:
                dealer_new_card = "King"
                dealer_score += 10
            elif dealer_new_card == 13:
                dealer_new_card = "Jack"
                dealer_score += 10
            elif dealer_new_card == 14:
                dealer_new_card = "Ace"
                if dealer_score < 11:
                    dealer_score += 11
                else:
                    dealer_score += 1
            else:
                dealer_score += dealer_new_card
            print("-----------------------------\nDealer's new card is: ", dealer_new_card, choice(card_type),
                  "\n-----------------------------")
            print("Dealer's score is:", dealer_score)
            print("Your score is:", player_score, )
            break
    while True:
        if dealer_score == 21:
            print("-----------\nYou Lose!!!\n-----------")
            break
        if player_score == 21:
            break
        if player_score > 21:
            break
        if dealer_score < 21 and dealer_score > player_score:
            print("-----------\nYou Lose!!!\n-----------")
            break
        elif dealer_score <= player_score:
            dealer_second_new_card = choice(card_value)
            if dealer_second_new_card == 11:
                dealer_second_new_card = "Queen"
                dealer_score += 10
            elif dealer_second_new_card == 12:
                dealer_second_new_card = "King"
                dealer_score += 10
            elif dealer_second_new_card == 13:
                dealer_second_new_card = "Jack"
                dealer_score += 10
            elif dealer_second_new_card == 14:
                if dealer_score > 10:
                    dealer_score += 1
                else:
                    dealer_score += 11
                dealer_second_new_card = "Ace"
            else:
                dealer_score += dealer_second_new_card
            print("-----------------------------\nDealer's new card is: ", dealer_second_new_card, choice(card_type),
                  "\n-----------------------------")
        elif dealer_score > 21:
            print("----------\nYou win!!!\n----------")
            break
        print("Dealers new score is", dealer_score)
        print("Your score is:", player_score)


card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
card_type = ["Clubs", "Diamonds", "Hearts", "Spades"]

while True:
    dealer_score = 0
    player_score = 0
    dealer_first_card = choice(card_value)
    dealer_card_type = choice(card_type)
    first_card = choice(card_value)
    second_card = choice(card_value)
    first_card_type = choice(card_type)
    second_card_type = choice(card_type)

    print(cardtype(dealer_first_card, dealer_card_type))
    dealer_score += scorecalulatordealer(dealer_first_card)
    print("Dealers score is:", dealer_score, '\n')

    print(cardtype(first_card, first_card_type))
    print(cardtype(second_card, first_card_type))
    player_score += scorecalulator(first_card)
    player_score += scorecalulator(second_card)
    print("Your score is:", player_score)

    hit_stand(player_score, dealer_score)
    play_again = input("Play again? (Y/N): ")
    play_again = play_again.capitalize()
    if play_again == "N":
        print("Thank you for playing")
        break
    elif play_again == "Y":
        print('\n\n')