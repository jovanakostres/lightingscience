import pandas as pd
import luxpy as lx # package for color science calculations 
# print('Luxpy version: ',lx.__VERSION__)
# version: v1.9.6
import numpy as np # fundamental package for scientific computing 
import matplotlib.pyplot as plt # package for plotting


spdData = pd.read_csv('.\data\spectrums.txt', sep=' |:', header=None, engine='python')
spdData.columns = ['Light','Channel','Value']
spdData['Luminance'] = spdData.apply(lambda x: float(lx.spd_to_power(eval(x['Value']), ptype='pu')), axis=1)
# spd_to_power(): spectral radiant power [W/nm] to luminance [cd/m^2]


for i in [1,2,3,5]:
    channel = []
    luminance = []
    for j in range(1,256,10):
        channel.append(j)
        luminance.append(spdData['Luminance'][spdData['Light']==i][spdData['Channel']==j])
    plt.figure()
    plt.plot(channel,luminance)
    plt.xlabel('Channel')
    plt.ylabel('Luminance[cd/m^2]')
    plt.show
   
#curvefitting
def ChannelValue(l:int, perc:float): #l:light(R-1,G-2,B-3,A-5), perc:percentage of the channel
    if l == 1:
        para = np.array([3.79101032e-03, -7.71247848e-02,9.17950337e+00])
        func = np.poly1d(para)
    elif l == 2:
        para = np.array([9.14054992e-03, -2.08932099e-01,2.49404590e+01])
        func = np.poly1d(para)
    elif l == 3:
        para = np.array([1.76936023e-03, -4.70784519e-02,4.83069050e+00])
        func = np.poly1d(para)
    elif l == 5:
        para = np.array([3.47076694e-03, -2.68425662e-02,8.62810845e+00])
        func = np.poly1d(para)
    
    return int([x for x in np.roots(func-perc*255) if x > 0][0])

print(ChannelValue(1,0.9))
