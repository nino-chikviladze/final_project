import random

SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def create_deck():
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck


def calculate_score(hand):
    score = 0
    for rank, _ in hand:
        if rank in ["J", "Q", "K"]:
            score += 10
        elif rank == "A":
            score += 11
        else:
            score += int(rank)
    return score


def display_hand(player_name, hand, score):
    cards_str = ", ".join([f"{rank} of {suit}" for rank, suit in hand])
    print(f"{player_name}'s hand: [{cards_str}] (Score: {score})")


def play_game():
    print("\n<--- New Round --->")
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    display_hand("Player", player_hand, player_score)

    while player_score < 21:
        choice = input("Do you want to add a card or stop? (add/stop): ").strip().lower()
        if choice == 'add':
            player_hand.append(deck.pop())
            player_score = calculate_score(player_hand)
            display_hand("Player", player_hand, player_score)
        elif choice == 'stop':
            break
        else:
            print("Invalid input. Please type 'add' or 'stop'.")

    if player_score > 21:
        print("\nYou busted! (Score > 21)")
        print("You lose")
        return

    print("\nComputer's turn...")
    display_hand("Computer", computer_hand, computer_score)

    while computer_score < 17:
        print("Computer drawing a card...")
        computer_hand.append(deck.pop())
        computer_score = calculate_score(computer_hand)
        display_hand("Computer", computer_hand, computer_score)

    print("\n--- Final Results ---")
    print(f"Your final score: {player_score}")
    print(f"Computer's final score: {computer_score}")

    if computer_score > 21:
        print("Computer busted! You win")
    elif player_score > computer_score:
        print("You win")
    elif computer_score > player_score:
        print("You lose")
    else:
        print("It's a tie! Redealing...")
        play_game()


if __name__ == "__main__":
    play_game()