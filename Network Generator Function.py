
# coding: utf-8

# In[65]:


import networkx as nx
import numpy as np

def network_generator(number, node, probability = None, neighbors = None):
    '''
    generate network from folowing network list
    networks = 2d-lattice, erdos-renyi, watts-strogatz small-word, scale-free
    
    ---- Parameters
    
    nember: number of network from list and started by 1. for example 1 refers to 2d-lattice
    
    node: number of network nodes. for 2d-lattice it should be a square of a number 
    
    probability: Probability for edge creation. it use for erdos_renyi and watts-strogatz small-word networks
    
    neighbors: The number of neighbors connected to each node in the watts-strogatz small-word network
    
    ---- return
    
    M: The adjacency matrix of chosen network
    
    '''
    
    if number == 1:
        n = m = np.sqrt(node)
        G = nx.generators.lattice.grid_2d_graph(m=m,n=n,periodic=True)
        
    if number == 2:
        G = nx.generators.random_graphs.erdos_renyi_graph(n=node,p=probability)
    
    if number == 3:
        G = nx.generators.random_graphs.watts_strogatz_graph(n=node,k=neighbors, p=probability)  
        
    if number == 4:
        G = nx.generators.directed.scale_free_graph(n=node)  
        
    M = nx.to_numpy_array(G)
    
    return M

