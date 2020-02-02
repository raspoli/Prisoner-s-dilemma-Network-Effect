import networkx as nx
import numpy as np

def network_generator(network_type, node, probability = None, neighbors = None):
    '''
    generate network from folowing network list
    networks = 2d-lattice, erdos-renyi, watts-strogatz small-world, scale-free

    ---- Parameters

    network_type: type of network from list and started by 1. for example 1 refers to 2d-lattice

    node: number of network nodes. for 2d-lattice it should be a squared integer

    probability: Probability for edge creation. it use for erdos_renyi and watts-strogatz small-word networks

    neighbors: The number of neighbors connected to each node in the watts-strogatz small-world network

    ---- return

    M: The adjacency matrix of the chosen network

    '''
    if network_type==1:
        G = nx.generators.lattice.grid_2d_graph(m=np.sqrt(node),n=n,periodic=True)
    elif network_type==2:
        G = nx.generators.random_graphs.erdos_renyi_graph(n=node,p=probability)
    elif network_type==3:
        G = nx.generators.random_graphs.watts_strogatz_graph(n=node,k=neighbors, p=probability)
    elif network_type==4:
        G = nx.generators.scale_free_graph(n=node)
    else
        G = nx.generators.random_graphs.erdos_renyi_graph(n=node,p=0.5)
        
    M = nx.to_numpy_array(G)

    return M
