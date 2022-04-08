#library imports
import luxpy as lx
from luxpy.toolboxes import spectro as sp
from luxpy.toolboxes.spectro import jeti as jeti

import time
import json
from DMXEnttecPro import Controller
dmx = Controller('COM8')  # Typical of Windows

# sp.jeti.set_laser(laser_on=True) #turning the laser on. The laser points to the target
# #sp.jeti.set_laser(laser_on=False)
# spd = sp.get_spd('jeti') #passing device name to get_spd function
# lx.SPD(spd).plot() #plotting the spd
# xyz = lx.spd_to_xyz(spd)
# Yuv = lx.xyz_to_Yuv(xyz)

spds = {}
spd = []
sp.jeti.set_laser(laser_on=True)  # turning the laser on. The laser points to the target

for i in [1,2,3,5]:
    for j in range(1,256,10):
        #time.sleep(1)

        dmx.set_channel(i, j)  # Sets DMX channel 1 to max 255
        dmx.submit()

        spectrum = sp.get_spd('jeti')  # passing device name to get_spd function
        print(lx.spd_to_xyz(spectrum))

        key = str(i) + ', ' + str(j)
        spds[key] = spectrum

    dmx.set_channel(i, 0)  # Sets DMX channel 1 to max 255
    dmx.submit()
    time.sleep(2)

print(spds)
sp.jeti.set_laser(laser_on=False)

with open("spectrums.txt", 'w') as f:
    for key, value in spds.items():
        f.write('%s:%s\n' % (key, value))

#print(Yuv)