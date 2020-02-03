import numpy as np

def strategy_assign(N,strategy_list,frac_list=0):
    '''
        distributes a list of strategies among agents
    ---- input
        N: number of agents
        strategy_list: strategies to distribute between agents, do not use zero
    ---- output
        S: list of strategies corresponding to each agent
    '''
    S=np.zeros(N)
    ns=len(strategy_list)
    if frac_list==0:
        frac_list=np.ones(N)
        frac_list*=1/ns
    last=0
   
    for s in range(ns):
        f=int(N*frac_list[s])
        S[last:f]=strategy_list[s]
        
        last=int(N*frac_list[s])
    S[np.where(S==0)]=strategy_list[np.random.randint(ns)]
    return S

n=16
s_list=[1 ,2 ,3 ,4]

s=strategy_assign(n , s_list , frac_list=0)
