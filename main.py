import numpy as np
from copy import deepcopy
from network_generator import network_generator
from strategy_assign import strategy_assign, m_strategy_assign
from Strategy_Matrix import Strategy_Matrix
from Update_Strategy import Update
from numbers_of_strategies import area
import matplotlib.pyplot as plt
from time_distribution import time_distribution
from plot_final import plot_final


#input
N=int(input("Enter the number of agents: "))
network_type=int(input("Choose network structure:   1) 2D lattice   2) Erdos-Renyi random graph 3) Watts-Strogatz small-world   4) Barabasi-Albert scale-free\n"))
network_parameter1=network_parameter2=0
if network_type==1:
    while np.sqrt(N)!=int(np.sqrt(N)):
        N=int(input("For a 2D lattice N should be square of an integer: "))
    net_name='2D lattice'
elif network_type==2:
    network_parameter1=4/N
    net_name='Erdos-Renyi'
elif network_type==3:
    network_parameter1=float(input("Enter re-routing probability: "))
    network_parameter2=4
    net_name='Small-World'
else:
    net_name='Barabasi-Albert'
beta=float(input("Enter beta:"))
max_seasons = int(input("total game time:"))

#generate network
adj=network_generator(network_type, N, network_parameter1, network_parameter2)

#assign strategies
total_strat=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
strat = m_strategy_assign(N,total_strat)
S=Strategy_Matrix()
dens=np.zeros((len(total_strat),max_seasons))
total_Reward = np.zeros(N)
for seasons in range(max_seasons):
    R=np.zeros(N)
    dens[:,seasons] = time_distribution(area(strat))
    for i, strat_i in enumerate(strat):
        neighbors_list_strat = strat[np.where(adj[i,:] == 1)[0]]
        R[i] = np.sum([S[int(strat_i),int(strat_j)] for strat_j in neighbors_list_strat])

    strat = Update(strat,R,beta)


    total_Reward += deepcopy(R)

plot_final(dens,max_seasons)
plt.title('Network type'=net_name)
