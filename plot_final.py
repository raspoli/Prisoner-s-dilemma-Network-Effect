import numpy as np
import matplotlib.pyplot as plt

def plot_final(L, max_seasons):

    x = [item for item in range(1, max_seasons + 1)]
    for i in range(int(len(L)/2)):
    # plt.plot(x,y1,x,y2,x,y3,x,y4,x,y5,x,y6,x,y7,x,y8,x,y9,x,y10,x,y11,x,y12,x,y13,x,y14,x,y15,x,y16)
        plt.plot(x,L[i,:])
    for i in range(int(len(L)/2)):
    # plt.plot(x,y1,x,y2,x,y3,x,y4,x,y5,x,y6,x,y7,x,y8,x,y9,x,y10,x,y11,x,y12,x,y13,x,y14,x,y15,x,y16)
        plt.plot(x,L[int(len(L)/2)+i,:],linestyle='--')
    plt.xlabel('time')
    plt.ylabel('Distribution of strategies')
    plt.title('evolve of strategies')
    # plt.legend(( 'strategy 1' , 'strategy 2' , 'strategy 3' , 'strategy 4' , 'strategy 5' , 'strategy 6' , 'strategy 7' , 'strategy 8' , 'strategy 9' , 'strategy 10' , 'strategy 11' , 'strategy 12' , 'strategy 13' , 'strategy 14' , 'strategy 15' , 'strategy 16'), loc='upper right')
    listt=['0000','0001','0010','0011','0100','0101',
                     '0110','0111','1000','1001','1010','1100',
                     '1011','1101','1110','1111']
    plt.legend(listt, loc='upper right')
    plt.ylim((0,1.1))
    plt.show()
