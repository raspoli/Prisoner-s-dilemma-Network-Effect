
# coding: utf-8

# In[1]:


import numpy as np
from itertools import combinations 
from copy import deepcopy
from sklearn.preprocessing import normalize


# In[23]:


def Reward(S1,S2):
    ep = 0
    S2 = deepcopy(S2[0] + S2[2] + S2[1] + S2[3])
    P0 = np.zeros((4,4))
    for i in range(8):
        for j in range(4):
            if i == 0:
                P0[i,j] = abs(int(S1[j])-ep) * abs(int(S2[j])-ep)
            elif i == 1:
                P0[i,j] = abs(int(S1[j])-ep) * (1-abs(int(S2[j])-ep))
            elif i == 2:
                P0[i,j] = (1-abs(int(S1[j])-ep)) * abs(int(S2[j]))
            elif i == 3:
                P0[i,j] = (1-abs(int(S1[j])-ep)) * (1-abs(int(S2[j])-ep))
                
    P = np.concatenate((P0,P0),axis = 1)
    P = np.concatenate((P,P),axis = 0)
    
    
    cc = np.array([1,1,1,1,0,0,0,0])
    cc = cc.reshape(1,8)
    ot = np.array([0,0,0,0,1,1,1,1])
    ot = ot.reshape(1,8)

    Q = np.transpose(np.concatenate((cc,ot,ot,ot,cc,ot,ot,ot)))
    
    P_f = P * Q
    
    
    return P_f


# In[22]:


def Strategy_Matrix(strategy_list = ['0000','0001','0010','0011','0100','0101',
                 '0110','0111','1000','1001','1010','1100',
                 '1011','1101','1110','1111'], b1 = 2, b2 = 1.2):
    
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
        re = bonus * v
        r = np.mean(re[re!=0])
        U.append(r)
    
###############################
    
    L = []
    for low in pair_list_low:
        p = Reward(low[0],low[1])

        w, v = np.linalg.eig(p)

        v = abs((v[:,np.where(w == 1)[0]])/(np.linalg.norm(v[:,np.where(w == 1)[0]],axis = 0,ord=1)))
        re = bonus * v
        r = np.mean(re[re!=0])
        L.append(r)  
        
###############################       
        
    D = []
    for d in strategy_list:
        p = Reward(d,d)

        w, v = np.linalg.eig(p)

        v = abs((v[:,np.where(w == 1)[0]])/(np.linalg.norm(v[:,np.where(w == 1)[0]],axis = 0,ord=1)))
        re = bonus * v
        r = np.mean(re[re!=0])
        D.append(r)
        
###############################

    S = np.zeros((l,l))

    S[np.triu_indices(l,1)] = L
    S = np.transpose(S)
    S[np.triu_indices(l,1)] = U
    np.fill_diagonal(S,D)
    
    
    
    return np.nan_to_num(S)
        


# In[21]:

### strategy = cc,cd,dc,dd
strategy_list = ['0000','0001','0010','0011','0100','0101',
                 '0110','0111','1000','1001','1010','1100',
                 '1011','1101','1110','1111']

