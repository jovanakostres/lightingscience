from DMXEnttecPro import Controller
import pandas as pd
import luxpy as lx # package for color science calculations
# print('Luxpy version: ',lx.__VERSION__)
# version: v1.9.6
import numpy as np # fundamental package for scientific computing
import matplotlib.pyplot as plt # package for plotting
import copy
from scipy import interpolate
from luxpy.toolboxes import spectro as sp
from luxpy.toolboxes.spectro import jeti as jeti

dmx = Controller('COM8')  # Typical of Windows

dmx.set_channel(1, 9)  # Sets DMX channel 1 to max 255

dmx.submit()
dmx.set_channel(2, 8)  # Sets DMX channel 1 to max 255

dmx.submit()
dmx.set_channel(3, 20)  # Sets DMX channel 1 to max 255

dmx.submit()
dmx.set_channel(5, 40)  # Sets DMX channel 1 to max 255

dmx.submit()


sp.jeti.set_laser(laser_on=True) #turning the laser on. The laser points to the target
# #sp.jeti.set_laser(laser_on=False)
spd = sp.get_spd('jeti') #passing device name to get_spd function
lx.SPD(spd).plot() #plotting the spd
plt.plot(spd[0],spd[1])
plt.show()
xyz = lx.spd_to_xyz(spd, relative=False)
#Yuv = lx.xyz_to_Yuv(xyz)
print(xyz)
Yxy = lx.xyz_to_Yxy(xyz)
print(Yxy)
print(lx.xyz_to_cct(xyz, out = 'cct,duv'))