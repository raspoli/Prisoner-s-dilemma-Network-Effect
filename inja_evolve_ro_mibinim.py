import numpy as np
import matplotlib.pyplot as plt

def evolve_bebinim(L, max_seasons):
    
    x = [item for item in range(1, max_seasons + 1)]
    
    y1 = []
    for i in range(max_seasons):
        y1.append(L[i][0])
    
    y2 = []
    for i in range(max_seasons):
        y2.append(L[i][1])
    
    y3 = []
    for i in range(max_seasons):
        y3.append(L[i][2])
    
    y4 = []
    for i in range(max_seasons):
        y4.append(L[i][3])
        
    y5 = []
    for i in range(max_seasons):
        y5.append(L[i][4])
    
    y6 = []
    for i in range(max_seasons):
        y6.append(L[i][5])
        
    y7 = []
    for i in range(max_seasons):
        y7.append(L[i][6])
        
    y8 = []
    for i in range(max_seasons):
        y8.append(L[i][7])
    
    y9 = []
    for i in range(max_seasons):
        y9.append(L[i][8])
        
    y10 = []
    for i in range(max_seasons):
        y10.append(L[i][9])
    
    y11 = []
    for i in range(max_seasons):
        y11.append(L[i][10])
        
    y12 = []
    for i in range(max_seasons):
        y12.append(L[i][11])
        
    y13 = []
    for i in range(max_seasons):
        y13.append(L[i][12])
        
    y14 = []
    for i in range(max_seasons):
        y14.append(L[i][13])
        
    y15 = []
    for i in range(max_seasons):
        y15.append(L[i][14])
        
    y16 = []
    for i in range(max_seasons):
        y16.append(L[i][15])
        
    plt.plot(x,y1,x,y2,x,y3,x,y4,x,y5,x,y6,x,y7,x,y8,x,y9,x,y10,x,y11,x,y12,x,y13,x,y14,x,y15,x,y16)
    plt.xlabel('time')
    plt.ylabel('Distribution of strategies')
    plt.title('evolve of strategies')
    plt.legend(( 'strategy 1' , 'strategy 2' , 'strategy 3' , 'strategy 4' , 'strategy 5' , 'strategy 6' , 'strategy 7' , 'strategy 8' , 'strategy 9' , 'strategy 10' , 'strategy 11' , 'strategy 12' , 'strategy 13' , 'strategy 14' , 'strategy 15' , 'strategy 16'), loc='upper right')
    plt.show()