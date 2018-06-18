import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        epsilon = 1.0/i_episode
        policy_s=np.ones(self.nA)*epsilon/self.nA
        policy_s[np.argmax(self.Q[state])] = 1-epsilon + (epsilon / self.nA)
        
        return np.random.choice(np.arange(self.nA,p=policy_s)
        #return np.random.choice(self.nA)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        Qsa = self.Q[state][action]
        Qsa_next = self.Q[next_state][next_action]
                                
        if not done :
             self.Q[state][action] = Qsa + (alpha * (reward +  Qsa_next) - Qsa)                   
        if done :
             self.Q[state][action] = Qsa + (alpha * (reward - Qsa))
