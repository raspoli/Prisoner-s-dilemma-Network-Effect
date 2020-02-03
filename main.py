import numpy as np
from network_generator import network_generator
from strategy_assign import strategy_assign
from Strategy_Matrix import Strategy_Matrix
from Update_Strategy import distribution_function, Update

#input
N=int(input("Enter the number of agents: "))
network_type=int(input("Choose network structure:   1) 2D lattice   2) Erdos-Renyi random graph 3) Watts-Strogatz small-world   4) Barabasi-Albert scale-free\n"))
network_parameter1=network_parameter2=0
if network_type==1:
    while np.sqrt(N)!=int(np.sqrt(N)):
        N=int(input("For a 2D lattice N should be square of an integer: "))
elif network_type==2:
    network_parameter1=float(input("Enter connection probability: "))
elif network_type==3:
    network_parameter1=float(input("Enter re-routing probability: "))
    network_parameter2=float(input("Enter initial number of neighbors: "))
beta=float(input("Enter beta:"))
#generate network
adj=network_generator(network_type, N, network_parameter1, network_parameter2)

#assign strategies
strat=strategy_assign(N,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
S=Strategy_Matrix()

def p(delta):
    return distribution_function(delta,beta)

fig, ax = plt.subplots(2,1)

for seasons in range(max_seasons):
    R=np.zeros(N)
    for i in range(N):
        strat_i=strat[i]
        neighbors_list=np.where(adj[i,:]==1)
        neighbors_list_strat=strat[neighbors_list]
        R[i]=np.sum([S[strat_i,strat_j] for strat_j in neighbors_list_strat])
        strat=Update(p,strat,R)
