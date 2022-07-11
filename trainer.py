from random import random

#  Setting up the game by defining the number of actions that
#  can be taken, as well as setting arbitrary values for RPS
ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3

# Tracks the sum of all regrets over all possible actions
regret_sum = [] * NUM_ACTIONS
strategy = [] * NUM_ACTIONS
strategy_sum = [NUM_ACTIONS]
opp_strategy = [1/3,1/3,1/3]


def get_strategy():
    global ROCK, PAPER, SCISSORS, NUM_ACTIONS, regret_sum,\
        strategy, strategy_sum, opp_strategy
    normalizing_sum = 0
    for i in range(NUM_ACTIONS):
        strategy[i] = regret_sum[i] if regret_sum[i] > 0 else 0
        normalizing_sum += strategy[i]
    for i in range(NUM_ACTIONS):
        if normalizing_sum > 0:
            strategy[i] /= normalizing_sum
        else:
            strategy[i] = 1.0 / NUM_ACTIONS
        strategy_sum += strategy[i]
    return strategy

def get_action(strategy):
    r = random()