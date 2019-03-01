# dice game
from itertools import combinations

def decide_winner(dice1, dice2):
  dice1_wins, dice2_wins = count_wins(dice1, dice2)
  if dice1_wins > dice2_wins:
    return 0
  else:
    return 1

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in range(6):
      for j in range(6):
        if dice1[i] > dice2[j]:
          dice1_wins += 1
        elif dice2[j] > dice1[i]:
          dice2_wins += 1
    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
  combs = combinations(range(len(dices)), 2)
  wins = [0] * len(dices)
  for c in combs:
    wins[c[decide_winner(dices[c[0]], dices[c[1]])]] += 1
  print(wins)

  max_wins = max(wins)
  number_of_dices_with_max_wins = 0
  for d in wins:
    if d == max_wins:
      number_of_dices_with_max_wins += 1
  if number_of_dices_with_max_wins > 1:
    return -1
  else:
    return wins.index(max_wins)

def determine_choice(dices, rival):
  for i in range(len(dices)):
    if dices[i] != rival and decide_winner(dices[i], rival) == 0:
      return i

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    strategy = dict()

    best_dice = find_the_best_dice(dices)
    if best_dice == -1:
      strategy["choose_first"] = False
      for i in range(len(dices)):
        strategy[i] = determine_choice(dices, dices[i])
    else:
      strategy["choose_first"] = True
      strategy["first_dice"] = best_dice

    return strategy
