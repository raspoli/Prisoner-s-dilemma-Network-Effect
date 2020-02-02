
# coding: utf-8

# In[1]:


import numpy as np
from itertools import combinations 
from copy import deepcopy
from sklearn.preprocessing import normalize


# In[2]:


def Reward(S1,S2):
    S2 = deepcopy(S2[0] + S2[2] + S2[1] + S2[3])
    P0 = np.zeros((4,4))
    for i in range(8):
        for j in range(4):
            if i == 0:
                P0[i,j] = int(S1[j]) * int(S2[j])
            elif i == 1:
                P0[i,j] = int(S1[j]) * (1-int(S2[j]))
            elif i == 2:
                P0[i,j] = (1-int(S1[j])) * int(S2[j])
            elif i == 3:
                P0[i,j] = (1-int(S1[j])) * (1-int(S2[j]))
                
    P = np.concatenate((P0,P0),axis = 1)
    P = np.concatenate((P,P),axis = 0)
    
    
    cc = np.array([1,1,1,1,0,0,0,0])
    cc = cc.reshape(1,8)
    ot = np.array([0,0,0,0,1,1,1,1])
    ot = ot.reshape(1,8)

    Q = np.transpose(np.concatenate((cc,ot,ot,ot,cc,ot,ot,ot)))
    
    P = P * Q
    
    
    return P


# In[14]:


def Strategy_Matrix(strategy_list = ['0000','0001','0010','0011','0100','0101',
                 '0110','0111','1000','1001','1010','1100',
                 '1011','1101','1110','1111'], b1 = 5, b2 = 3):
    
    l = len(strategy_list)

    pair_list_up = list(combinations(strategy_list, 2))

    pair_list_low = []
    for p in pair_list_up:
        pair_list_low.append((p[1],p[0]))

    
    bonus = np.array([b1-1,-1,b1,0,b2-1,-1,b2,0]).reshape(8,1)
    
    
    
    U = []
    for up in pair_list_up:
        p = Reward(up[0],up[1])

        w, v = np.linalg.eig(p)

        v = abs((v[:,np.where(w == 1)[0]])/(np.linalg.norm(v[:,np.where(w == 1)[0]],axis = 0,ord=1)))
        r = np.sum(bonus * v)
        U.append(r)
    
###############################
    
    L = []
    for low in pair_list_low:
        p = Reward(low[0],low[1])

        w, v = np.linalg.eig(p)

        v = abs((v[:,np.where(w == 1)[0]])/(np.linalg.norm(v[:,np.where(w == 1)[0]],axis = 0,ord=1)))
        r = np.sum(bonus * v)
        L.append(r)  
        
###############################       
        
    D = []
    for d in strategy_list:
        p = Reward(d,d)

        w, v = np.linalg.eig(p)

        v = abs((v[:,np.where(w == 1)[0]])/(np.linalg.norm(v[:,np.where(w == 1)[0]],axis = 0,ord=1)))
        r = np.sum(bonus * v)
        D.append(r)
        
###############################

    S = np.zeros((l,l))

    S[np.triu_indices(l,1)] = U
    np.fill_diagonal(S,D)
    S[np.tril_indices(l,-1)] = L
    
    
    
    return S
        


# In[11]:


### strategy = cc,cd,dc,dd
strategy_list = ['0000','0001','0010','0011','0100','0101',
                 '0110','0111','1000','1001','1010','1100',
                 '1011','1101','1110','1111']

