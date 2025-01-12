from typing import Dict 

def find_arbitrage_opps(pos_moneylines: Dict[str, float], neg_moneylines: Dict[str, float]):

    min_pos, min_pos_value = None, float('inf')
    for sportsbook, line in pos_moneylines.items():
        if line > 0:
            implied_prob = abs(line) / (100 + abs(line))
            if implied_prob < min_pos_value:
                min_pos, min_pos_value = sportsbook, implied_prob

    min_neg, min_neg_value = None, float('inf')
    for sportsbook, line in neg_moneylines.items():
        if line < 0:
            implied_prob = 100 / (100 + abs(line))
            if implied_prob < min_neg_value:
                min_neg, min_neg_value = sportsbook, implied_prob

    if min_neg_value + min_pos_value < 1:
        print(f"Arbitrage Opportunity Found!")

        total = min_neg_value + min_pos_value
        pos_stake = min_neg_value / total * 100
        neg_stake = min_pos_value / total * 100
    
        print(f"Bet {pos_stake:.2f}% on {min_pos} at {pos_moneylines[min_pos]}")
        print(f"Bet {neg_stake:.2f}% on {min_neg} at {neg_moneylines[min_neg]}")
        print(f"Expected Return: {(100 / total - 100):.2f}%")

    else:
        print("No Arbitrage Opportunity Found")


if __name__ == "__main__":

    pos_moneylines = {
        "sportsbook1": 130,
        "sportsbook2": 500,
        "sportsbook3": 600
    }

    neg_moneylines = {
        "sportsbook4": -200,
        "sportsbook5": -800,
        "sportsbook6": -120
    }

    find_arbitrage_opps(pos_moneylines, neg_moneylines)
    