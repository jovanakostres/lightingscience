import pandas as pd
import luxpy as lx # package for color science calculations 
# print('Luxpy version: ',lx.__VERSION__)
# version: v1.9.6
import numpy as np # fundamental package for scientific computing 
import matplotlib.pyplot as plt # package for plotting
from scipy import interpolate



spdData = pd.read_csv('.\data\spectrums.txt', sep=' |:', header=None, engine='python')
spdData.columns = ['Light','Channel','Value']
spdData['Luminance'] = spdData.apply(lambda x: float(lx.spd_to_power(eval(x['Value']), ptype='pu')), axis=1)
# spd_to_power(): spectral radiant power [W/nm] to luminance [cd/m^2]

largestLum = []
for i in [1,2,3,5]:
    channel = []
    luminance = []
    col = np.where(i==1, 'r', np.where(i==2, 'g', np.where(i==3, 'b', 'y')))
    for j in range(1,256,10):
        channel.append(j)
        luminance.append(spdData['Luminance'][spdData['Light']==i][spdData['Channel']==j])
    
    largestLum.append(float(luminance[-1]))    # record the largest luminance of every channel
    plt.plot(channel,luminance,str(col),label='light:'+str(col))
    plt.legend()
    plt.xlabel('Value')
    plt.ylabel('Luminance[cd/m^2]')
    plt.title('Relation between Value of Channel and Luminance')
    plt.show    #plot
    
    x = np.array(channel)
    y = np.array(luminance)    
    exec('func'+str(i)+'=interpolate.UnivariateSpline(y,x,s=0)') # interpolation: pass all the points

largestLum.insert(3,None) #To easily process in function of ChannelValue


def ChannelValue(l:int, perc:float): 
    # input: l:light(R-1,G-2,B-3,A-5), perc:the percentage of the maximum luminance of the channel
    # output: the channel value(1~251)
    return int(eval('func'+str(l)+'('+str(perc*largestLum[l-1])+')'))        