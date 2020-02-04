# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:19:47 2020

@author: asus
"""

import numpy as np
import matplotlib.pyplot as plt


def area(strategy_list):
    '''return a list of numbers of strategies
    ---- input : strategy list
    ---- out put :list of numbers of each strategy
    '''
    unique_elements, counts_elements = np.unique(strategy_list, return_counts=True)

    L=np.zeros(16)
    for i in unique_elements:
        L[i]=counts_elements[np.where(unique_elements==i)]

    return L
