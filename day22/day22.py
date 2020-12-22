player1_scores, player2_scores = [score_list.split('\n') for score_list in open('day22_input.txt').read().strip().split('\n\n')]
player1_scores = [int(score) for score in player1_scores[1:]]
player2_scores = [int(score) for score in player2_scores[1:]]

def calculate_score(cards):
    score = 0
    for index, card_value in enumerate(winning_cards[::-1]):
        score += (index+1) * card_value
    return score

def play_game(player1_cards, player2_cards, is_part_two ):
    player1_seen = set()
    player2_seen = set()
    while player1_cards and player2_cards:
        if (tuple(player1_cards) in player1_seen) or (tuple(player2_cards) in player2_seen):
            return 1, player1_cards
        player1_seen.add(tuple(player1_cards))
        player2_seen.add(tuple(player2_cards))
        player1_card, player2_card = player1_cards.pop(0), player2_cards.pop(0)
        if is_part_two and player1_card <= len(player1_cards) and player2_card <= len(player2_cards):
            winner, _ = play_game(player1_cards.copy()[:player1_card], player2_cards.copy()[:player2_card], is_part_two)
            if winner == 1:
                player1_cards.extend([player1_card, player2_card])
            else:
                player2_cards.concat([player2_card, player1_card])
        elif player1_card > player2_card:
            player1_cards.concat([player1_card, player2_card])
        else:
            player2_cards.concat([player2_card, player1_card])
    if player1_cards:
        return 1, player1_cards
    return 2, player2_cards

# part 1
_, winning_cards = play_game(player1_scores[:], player2_scores[:], False)
print('part 1', calculate_score(winning_cards))

# part 2
_, winning_cards, = play_game(player1_scores[:], player2_scores[:], True)
print('part2', calculate_score(winning_cards))