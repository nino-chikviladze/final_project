import logging
from random import randint, sample

logging.basicConfig(
    filename='lottery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

JACKPOT = randint(2, 80) * 1000000


def play_lottery():
    print("<----- Lottery Simulator ----->")
    
    # print("Enter 6 unique numbers (1-49):")
    # player_nums = set()
    # for i in range(1, 7):
    #     player_nums.add(int(input(f"Enter number {i}: ")))
    
    player_nums = set(map(int, input("Enter 6 unique numbers (1-49): ").split()))
    winning_nums = set(sample(range(1, 50), 6))
    print()

    matches = len(winning_nums.intersection(player_nums))

    match matches:
        case 6:
            prize = JACKPOT
        case 5:
            prize = JACKPOT * 0.6
        case 4:
            prize = JACKPOT * 0.4
        case 3:
            prize = JACKPOT * 0.2
        case _:
            prize = 0

    print("<------------ RESULTS ------------>")
    print(f"Jackpot:          ${JACKPOT:,}")
    print("Winning Numbers: ", *sorted(winning_nums), sep=" ")
    print("Your Numbers:    ", *sorted(player_nums), sep=" ")
    print(f"Matches:          {matches}")
    print(f"Prize Won:        ${prize:,.0f}")
    print("-----------------------------------")


    logging.info(
        f"Jackpot: ${JACKPOT:,} | "
        f"Winning Numbers: {sorted(winning_nums)} | "
        f"Player Numbers: {sorted(player_nums)} | "
        f"Matches: {matches} | "
        f"Payout: ${prize:,.0f}"
    )


if __name__ == "__main__":
    play_lottery()