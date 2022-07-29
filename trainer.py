from random import random

#  Setting up the game by defining the number of actions that
#  can be taken, as well as setting arbitrary values for RPS
ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3


class rpstrainer():
    def __init__(self, opp_strat):
        # Tracks the sum of all regrets over all possible actions
        self.regret_sum = [0] * NUM_ACTIONS
        self.strategy = [0] * NUM_ACTIONS
        self.strategy_sum = [0] * NUM_ACTIONS
        if abs(sum(opp_strat)-1) > 10e-8:
            raise Exception('sum of opponent\'s strategy must be 1')
        self.opp_strategy = [a for a in opp_strat]

    def get_strategy(self):
        global ROCK, PAPER, SCISSORS, NUM_ACTIONS
        normalizing_sum = 0
        for i in range(NUM_ACTIONS):
            self.strategy[i] = self.regret_sum[i] if self.regret_sum[i] > 0 else 0
            normalizing_sum += self.strategy[i]
        for i in range(NUM_ACTIONS):
            if normalizing_sum > 0:
                self.strategy[i] /= normalizing_sum
            else:
                self.strategy[i] = 1.0 / NUM_ACTIONS
            self.strategy_sum[i] += self.strategy[i]

    def get_action(self, strategy):
        r = random()
        i = 0
        cum_prob = 0
        while i < NUM_ACTIONS - 1:
            cum_prob += strategy[i]
            if r < cum_prob:
                break
            i += 1
        return i

    def train(self, iterations):
        a_util = [0] * NUM_ACTIONS
        for i in range(iterations):
            self.get_strategy()
            my_action =  self.get_action(self.strategy)
            other_action = self.get_action(self.opp_strategy)
            a_util[other_action] = 0
            a_util[0 if other_action == NUM_ACTIONS - 1 else other_action + 1] = 1
            a_util[NUM_ACTIONS - 1 if other_action == 0 else other_action - 1] = -1

            for j in range(NUM_ACTIONS):
                self.regret_sum[j] += a_util[j] - a_util[my_action]
    
    def get_average_strategy(self):
        avg_strat = [0] * NUM_ACTIONS
        norm_sum = 0
        for i in range(NUM_ACTIONS):
            norm_sum += self.strategy_sum[i]
        for i in range(NUM_ACTIONS):
            if norm_sum > 0:
                avg_strat[i] = self.strategy_sum[i] / norm_sum
            else:
                avg_strat[i] = 1 / NUM_ACTIONS
        return avg_strat

if __name__ == '__main__':
    trainer = rpstrainer([0.34,0.33,0.33])
    trainer.train(100000)
    print(trainer.get_average_strategy())

