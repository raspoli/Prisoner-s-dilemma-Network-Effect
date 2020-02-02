# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:34:37 2020

@author: asus
"""

import numpy as np
import matplotlib.pyplot as plt


def histogram(strategy_list_1 , strategy_list_2,strategy_list_3,strategy_list_4):
    
    '''return a histogram of distribution of different strategies in final level in different networkx
    ---- input : strategy lists in final level
    ---- out put :histogram
    '''
    
    plt.hist(strategy_list_1,  label='network_1')
    plt.hist(strategy_list_2,  label='network_2')
    plt.hist(strategy_list_3,  label='network_3')
    plt.hist(strategy_list_4,  label='network_4')
    plt.title("distribution of strategies in different networks")
    plt.xlabel("strategies")
    plt.ylabel("distribution")
    plt.legend(loc='upper right')
    plt.show()
    
