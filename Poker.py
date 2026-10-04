import random 
import itertools

all_cards = ["DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", 
             "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", 
             "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", 
             "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",]

odds_of_pair=0
odds_of_twopair=0
odds_of_threeofkind=0
odds_of_straight=0
odds_of_flush=0
odds_of_fullhouse=0
odds_of_fourofakind=0
odds_of_sflush=0
odds_of_rflush=0

num_of_players= input("Input the number of players")

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
if len(ranks) != len(set(ranks)):
    odds_of_pair = 1*100
    if card1rank == card2rank:
        odds_of_threeofkind = 0.0426*100
    else:
        odds_of_threeofkind = 0.0842*100

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

print("odds of pair:", odds_of_pair,"%")
print("odds of three of a kind:", odds_of_threeofkind,"%")
print("odds of straight:", odds_of_straight,"%")
print("odds of flush:", odds_of_flush)
print("odds of fullhouse:", odds_of_fullhouse)
change1