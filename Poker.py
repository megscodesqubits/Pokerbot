import itertools
from collections import Counter
import random

all_cards = ["DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", 
             "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", 
             "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", 
             "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",]

odds_of_pair=0
odds_of_twopair=0
odds_of_threeofakind=0
odds_of_straight=0
odds_of_flush=0
odds_of_fullhouse=0
odds_of_fourofakind=0
odds_of_sflush=0
odds_of_rflush=0

card1 = input("Input the first card")
card1suit = card1[0]
card1rank = card1[1:]
all_cards.remove(card1)
card2 = input("Input the second card")
card2suit = card2[0]
card2rank = card2[1:]
all_cards.remove(card2)

tcard1 = input("Input the first card on the table")
tcard1suit = tcard1[0]
tcard1rank = tcard1[1:]
all_cards.remove(tcard1)
tcard2 = input("Input the second card on the table")
tcard2suit = tcard2[0]
tcard2rank = tcard2[1:]
all_cards.remove(tcard2)
tcard3 = input("Input the third card on the table")
tcard3suit = tcard3[0]
tcard3rank = tcard3[1:]
all_cards.remove(tcard3)

known_cards = [card1, card2, tcard1, tcard2, tcard3]
remaining_cards = [card for card in all_cards if card not in known_cards]

ranks = [card1rank, card2rank, tcard1rank, tcard2rank, tcard3rank]
#Odds for pair and three of a kind
def has_pair(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1:])
    for rank in set(ranks):
        if ranks.count(rank) >=2:
            return True
    return False
def has_threeofakind(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1:])
    for rank in set(ranks):
        if ranks.count(rank) >= 3:
            return True
    return False

total_combinations =0
pair_combinations=0
threeofakind_combinations=0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations +=1
    final_cards = known_cards + [turn, river]
    if has_pair(final_cards):
        pair_combinations +=1
    if has_threeofakind(final_cards):
        threeofakind_combinations+=1
odds_of_pair = (pair_combinations/total_combinations)*100
odds_of_threeofakind = (threeofakind_combinations/total_combinations)*100

#Odds of two pair
def has_twopair(cards):
    ranks = []
    for card in cards:
        ranks.append(card[1:])
    pair_count = 0
    for rank in set(ranks):
        if ranks.count(rank) >= 2:
            pair_count += 1
    if pair_count >= 2:
        return True
    return False
total_combinations = 0
twopair_combinations = 0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations += 1
    final_cards = known_cards + [turn, river]
    if has_twopair(final_cards):
        twopair_combinations += 1
odds_of_twopair = (twopair_combinations / total_combinations) * 100

#Odds of straights
def has_straight(cards):
    ranks1 = []
    for card in cards:
        rank = card[1:]
        if rank == "A":
            value = 14
        elif rank == "K":
            value = 13
        elif rank == "Q":
            value = 12
        elif rank == "J":
            value = 11
        else:
            value = int(rank)
        ranks1.append(value)
    ranks1 = list(set(ranks1))
    if 14 in ranks1:
        ranks1.append(1)
    ranks1.sort()
    for i in range(len(ranks1) - 4):
        if (ranks1[i+1] == ranks1[i] + 1 and
            ranks1[i+2] == ranks1[i] + 2 and
            ranks1[i+3] == ranks1[i] + 3 and
            ranks1[i+4] == ranks1[i] + 4):
            return True
    return False
total_combinations = 0
straight_combinations = 0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations += 1
    final_cards = known_cards + [turn, river]
    if has_straight(final_cards):
        straight_combinations += 1
odds_of_straight = (straight_combinations / total_combinations)*100

#Odds of flush
def has_flush(cards):
    suits = []
    for card in cards: 
        suit = card[0]
        suits.append(suit)
    for suit in ["D", "S", "H", "C"]:
        if suits.count(suit) >= 5:
            return True
    return False
total_combinations=0
flush_combinations=0
for turn, river in itertools.combinations(remaining_cards,2):
    total_combinations +=1
    final_cards = known_cards + [turn, river]
    if has_flush(final_cards):
        flush_combinations+=1
odds_of_flush = (flush_combinations/total_combinations)*100

# Odds of full house
def has_fullhouse(cards):
    ranks = []
    for card in cards:
        rank = card[1:]
        ranks.append(rank)
    rank_counts = []
    for rank in set(ranks):
        rank_counts.append(ranks.count(rank))
    if 3 in rank_counts and 2 in rank_counts:
        return True
    if rank_counts.count(3) >= 2:
        return True
    return False
total_combinations = 0
fullhouse_combinations = 0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations += 1
    final_cards = known_cards + [turn, river]
    if has_fullhouse(final_cards):
        fullhouse_combinations += 1
odds_of_fullhouse = (fullhouse_combinations / total_combinations) * 100

#Odds of four of a kind
def has_fourofakind(cards):
    ranks=[]
    for card in cards:
        ranks.append(card[1:])
    for rank in set(ranks):
        if ranks.count(rank) >= 4:
            return True
    return False
total_combinations=0
fourofakind_combinations=0
for turn, river in itertools.combinations(remaining_cards,2):
    total_combinations+=1
    final_cards = known_cards + [turn, river]
    if has_fourofakind(final_cards):
        fourofakind_combinations+=1
odds_of_fourofakind = (fourofakind_combinations/total_combinations)*100

#Odds of straight flush
def has_straightflush(cards):
    suits = ["D", "S", "H", "C"]
    for suit in suits:
        suited_cards = []
        for card in cards:
            if card[0] == suit:
                suited_cards.append(card)
        if len(suited_cards) <5:
            continue
        ranks = []
        for card in suited_cards:
            rank=card[1:]
            if rank == "A":
                value = 14
            elif rank == "K":
                value = 13
            elif rank == "Q":
                value = 12
            elif rank == "J":
                value = 11
            else: 
                value = int(rank)
            ranks.append(value)
        ranks = list(set(ranks))
        if 14 in ranks: 
            ranks.append(1)
        ranks.sort()
        for i in range(len(ranks) -4):
            if (ranks[i+1] == ranks[i] +1 and
                ranks[i+2] == ranks[i] +2 and
                ranks[i+3] == ranks[i] +3 and
                ranks[i+4] == ranks[i] +4):
                return True
    return False
total_combinations=0
sflush_combinations=0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations+=1
    final_cards = known_cards + [turn, river]
    if has_straightflush(final_cards):
        sflush_combinations+=1
odds_of_sflush = (sflush_combinations/total_combinations)*100

#Odds of royal flush
def has_royalflush(cards):
    suits = ["D", "S", "H", "C"]
    for suit in suits:
        needed_cards = [
            suit + "10",
            suit + "J",
            suit + "Q",
            suit + "K",
            suit + "A"]
        if all(card in cards for card in needed_cards):
            return True
    return False
total_combinations = 0
rflush_combinations = 0
for turn, river in itertools.combinations(remaining_cards, 2):
    total_combinations += 1
    final_cards = known_cards + [turn, river]
    if has_royalflush(final_cards):
        rflush_combinations += 1
odds_of_rflush = (rflush_combinations / total_combinations) * 100

def evaluate_hand(cards):
    ranks = []
    for card in cards:
        rank = card[1:]
        if rank == "A":
            value = 14
        elif rank == "K":
            value = 13
        elif rank == "Q":
            value = 12
        elif rank == "J":
            value = 11
        else:
            value = int(rank)
        ranks.append(value)
    suits = [card[0] for card in cards]
    rank_counts = Counter(ranks)
    flush_suit = None
    for suit in ["D", "S", "H", "C"]:
        if suits.count(suit) >= 5:
            flush_suit = suit
            break
    unique_ranks = sorted(set(ranks), reverse=True)
    if 14 in unique_ranks:
        unique_ranks.append(1)
    straight_high = None
    for i in range(len(unique_ranks) - 4):
        five = unique_ranks[i:i+5]
        if five[0] - five[4] == 4:
            straight_high = five[0]
            break
    if flush_suit is not None:
        suited_ranks = []
        for card in cards:
            if card[0] == flush_suit:
                rank = card[1:]
                if rank == "A":
                    value = 14
                elif rank == "K":
                    value = 13
                elif rank == "Q":
                    value = 12
                elif rank == "J":
                    value = 11
                else:
                    value = int(rank)
                suited_ranks.append(value)
        suited_ranks = sorted(set(suited_ranks), reverse=True)
        if 14 in suited_ranks:
            suited_ranks.append(1)
        for i in range(len(suited_ranks) - 4):
            five = suited_ranks[i:i+5]
            if five[0] - five[4] == 4:
                high = five[0]
                if high == 14:
                    return (9, 14)
                return (8, high)
    four = sorted(
        [rank for rank, count in rank_counts.items() if count == 4],
        reverse=True)
    if four:
        four_rank = four[0]
        kickers = sorted(
            [rank for rank in ranks if rank != four_rank],
            reverse=True)
        return (7, four_rank, kickers[0])
    triples = sorted(
        [rank for rank, count in rank_counts.items() if count >= 3],
        reverse=True)
    if triples:
        triple = triples[0]
        pairs = sorted(
            [rank for rank, count in rank_counts.items()
            if count >= 2 and rank != triple ],
            reverse=True   )
        if len(triples) >= 2:
            pairs.append(triples[1])
        if pairs:
            return (6, triple, max(pairs))
    if flush_suit is not None:
        flush_cards = []
        for card in cards:
            if card[0] == flush_suit:
                rank = card[1:]
                if rank == "A":
                    value = 14
                elif rank == "K":
                    value = 13
                elif rank == "Q":
                    value = 12
                elif rank == "J":
                    value = 11
                else:
                    value = int(rank)
                flush_cards.append(value)
        flush_cards.sort(reverse=True)
        return (5, *flush_cards[:5])
    if straight_high is not None:
        return(4, straight_high)
    if triples:
        triple = triples[0]
        kickers = sorted(
            [rank for rank in ranks if rank != triple],
            reverse=True)
        return (3, triple, *kickers[:2])
    pairs = sorted(
        [rank for rank, count in rank_counts.items() if count >= 2],
        reverse=True)
    if len(pairs) >= 2:
        high_pair = pairs[0]
        low_pair = pairs[1]
        kickers = sorted(
            [rank for rank in ranks
            if rank != high_pair and rank != low_pair],
            reverse=True)
        return (2, high_pair, low_pair, kickers[0])
    if len(pairs) == 1:
        pair = pairs[0]
        kickers = sorted(
            [rank for rank in ranks if rank != pair],
            reverse=True)
        return (1, pair, *kickers[:3])
    return (0, *sorted(ranks, reverse=True)[:5])

def win_probability(known_cards, remaining_cards, simulations=100000):
    wins = 0
    ties = 0
    losses = 0
    your_cards = known_cards[:2]
    board = known_cards[2:]
    for _ in range(simulations):
        opponent_cards = random.sample(remaining_cards, 2)
        available = [
            card for card in remaining_cards
            if card not in opponent_cards]
        cards_needed = 5 - len(board)
        future_cards = random.sample(available, cards_needed)
        final_board = board + future_cards
        your_final_cards = your_cards + final_board
        opponent_final_cards = opponent_cards + final_board
        your_score = evaluate_hand(your_final_cards)
        opponent_score = evaluate_hand(opponent_final_cards)
        if your_score > opponent_score:
            wins += 1
        elif your_score == opponent_score:
            ties += 1
        else:
            losses += 1
    odds_of_winning = (wins / simulations) * 100
    return odds_of_winning
odds_of_winning = win_probability(known_cards, remaining_cards)
print("")
print("odds of pair:", round(odds_of_pair,2),"%")
print("odds of two pair:", round(odds_of_twopair,2), "%")
print("odds of three of a kind:", round(odds_of_threeofakind,2),"%")
print("odds of straight:", round(odds_of_straight,2),"%")
print("odds of flush:", round(odds_of_flush,2),"%")
print("odds of fullhouse:", round(odds_of_fullhouse,2),"%")
print("odds of four of a kind:", round(odds_of_fourofakind,2), "%")
print("odds of straight flush:", round(odds_of_sflush,2),"%")
print("odds of royal flush:", round(odds_of_rflush,2), "%")
print("odds of winning:", round(odds_of_winning), "%")

tcard4 = input("Input the fourth card on the table:")
all_cards.remove(tcard4)
known_cards.append(tcard4)
remaining_cards = [card for card in all_cards if card not in known_cards]
odds_of_winning = win_probability(known_cards, remaining_cards)
total_combinations=0
pair_combinations=0
twopair_combinations=0
threeofakind_combinations=0
straight_combinations=0
flush_combinations=0
fullhouse_combinations=0
fourofakind_combinations=0
sflush_combinations=0
rflush_combinations=0
for river in all_cards:
    total_combinations +=1
    final_cards = known_cards + [river]
    if has_pair(final_cards):
        pair_combinations+=1
    if has_twopair(final_cards):
        twopair_combinations+=1
    if has_threeofakind(final_cards):
        threeofakind_combinations+=1
    if has_straight(final_cards):
        straight_combinations+=1
    if has_flush(final_cards):
        flush_combinations+=1
    if has_fullhouse(final_cards):
        fullhouse_combinations+=1
    if has_fourofakind(final_cards):
        fourofakind_combinations+=1
    if has_straightflush(final_cards):
        sflush_combinations+=1
    if has_royalflush(final_cards):
        rflush_combinations+=1
odds_of_pair = (pair_combinations / total_combinations) * 100
odds_of_twopair = (twopair_combinations / total_combinations) * 100
odds_of_threeofakind = (threeofakind_combinations / total_combinations) * 100
odds_of_straight = (straight_combinations / total_combinations) * 100
odds_of_flush = (flush_combinations / total_combinations) * 100
odds_of_fullhouse = (fullhouse_combinations / total_combinations) * 100
odds_of_fourofakind = (fourofakind_combinations / total_combinations) * 100
odds_of_sflush = (sflush_combinations / total_combinations) * 100
odds_of_rflush = (rflush_combinations / total_combinations) * 100
print("")
print("odds of pair:", round(odds_of_pair,2),"%")
print("odds of two pair:", round(odds_of_twopair,2), "%")
print("odds of three of a kind:", round(odds_of_threeofakind,2),"%")
print("odds of straight:", round(odds_of_straight,2),"%")
print("odds of flush:", round(odds_of_flush,2),"%")
print("odds of fullhouse:", round(odds_of_fullhouse,2),"%")
print("odds of four of a kind:", round(odds_of_fourofakind,2), "%")
print("odds of straight flush:", round(odds_of_sflush,2),"%")
print("odds of royal flush:", round(odds_of_rflush,2), "%")
print("odds of winning after river:", round(odds_of_winning, 2), "%")

tcard5 = input("Input the fifth card on the table:")
all_cards.remove(tcard5)
known_cards.append(tcard5)
remaining_cards = [card for card in all_cards if card not in known_cards]
odds_of_winning = win_probability(known_cards, remaining_cards)
final_cards=known_cards
if has_pair(final_cards):
    print("You have a pair!")
if has_twopair(final_cards):
    print("You have two pair!")
if has_threeofakind(final_cards):
    print("You have three of a kind!")
if has_straight(final_cards):
    print("You have a straight!")
if has_flush(final_cards):
    print("You have a flush!")
if has_fullhouse(final_cards):
    print("You have a fullhouse!")
if has_fourofakind(final_cards):
    print("You have four of a kind!")
if has_straightflush(final_cards):
    print("You have a straight flush!")
if has_royalflush(final_cards):
    print("You have a royal flush!")
print("odds of winning:", round(odds_of_winning, 2), "%")