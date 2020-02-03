import numpy as np

def time_distribution(distribution):
    
    d = np.array(distribution)

    s_u_m = np.sum(d)
    d = d/s_u_m
    
    return d
