import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

def create_deck():
    return [{'rank': rank, 'suit': suit, 'value': values[rank]} for suit in suits for rank in ranks]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    ace_count = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(name, hand):
    cards = ', '.join(f"{card['rank']} of {card['suit']}" for card in hand)
    print(f"{name}'s hand: {cards} (Total: {calculate_hand_value(hand)})")

def play_blackjack():
    money = 1000  # Starting money
    while money > 0:
        print(f"You have ${money}.")
        bet = int(input("Enter your bet: "))
        if bet > money or bet <= 0:
            print("Invalid bet. Try again.")
            continue
        
        deck = create_deck()
        random.shuffle(deck)
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        while True:
            display_hand('Player', player_hand)
            display_hand('Dealer', [dealer_hand[0]])  # Show only one dealer card
            
            if calculate_hand_value(player_hand) == 21:
                print("Blackjack! You win!")
                money += bet * 1.5
                break
            
            choice = input("Do you want to (H)it or (S)tand? ").lower()
            if choice == 'h':
                player_hand.append(deal_card(deck))
                if calculate_hand_value(player_hand) > 21:
                    display_hand('Player', player_hand)
                    print("Bust! You lose.")
                    money -= bet
                    break
            else:
                break
        
        if calculate_hand_value(player_hand) <= 21:
            print("Dealer's turn...")
            display_hand('Dealer', dealer_hand)
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))
                display_hand('Dealer', dealer_hand)
            
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            
            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
                money += bet
            elif player_value < dealer_value:
                print("Dealer wins!")
                money -= bet
            else:
                print("It's a tie!")
        
        if money == 0:
            print("You're out of money! Game over.")
            break

if __name__ == "__main__":
    play_blackjack()
