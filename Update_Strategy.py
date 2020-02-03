
# coding: utf-8

# In[29]:


import numpy as np
from copy import deepcopy

def distribution_function(delta_reward, betha):
    '''
    Defalt distribution for evolve strategy
    p = 1 / (1 + e^(-betha * delta_reward)
    ---- paramter
    delta_reward: difference of reward with maximum reward
    betha: distribution parameter

    ---- return
    evolution probability
    '''
    return (1 / (1 + np.exp(-betha * delta_reward)))

def Update(distribution, strategy_list, reward_list , betha):
    '''
    update strategies to winner strategiy by distribution

    ---- parameter
    distribution: function of evolution perobability distribution
    strategy_list: list of each person strategy
    reward_list: list of each person reward
    betha: distribution parameter

    ---- return
    updated strategy_list
    '''

    winer_strategy = deepcopy(strategy_list[np.argmax(reward_list)])
    rewards = deepcopy(reward_list)
    max_reward = max(rewards)
    difference_list = np.array(rewards) - max_reward
    evolve_distribution = distribution(difference_list, betha)
    help_probability = np.random.rand(len(evolve_distribution))
    evolve_chance = (evolve_distribution > help_probability)
    
    strategy_list[np.where(evolve_chance == 1)[0]] = winer_strategy
    
    return strategy_list


