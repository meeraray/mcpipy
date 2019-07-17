import sys
sys.path.insert(0, 'C:/Users/ronuk/AppData/Roaming/.minecraft/mcpipy')

from mine import *
import math
import coords
mc = Minecraft()

x1, y1, z1 = input("Enter x1 y1 z1: ").split()
x2, y2, z2 = input("Enter x2 y2 z2: ").split()
x1 = int(x1)
y1 = int(y1)
z1 = int(z1)
x2 = int(x2)
y2 = int(y2)
z2 = int(z2)

amp = (y2 - y1) / 2
baseline = (y1 + y2) / 2
print(amp)


if(z1 == z2):
	inc = 1
	if(x1 > x2):
		inc = -1
	for x in range(x1, x2, inc):
		y = amp * math.sin(1/math.pi * (x - x1)) + baseline
		y = round(y)
		print(x, y, z1)
		a, b, c = coords.mcToPy(x, y, z1)
		mc.setBlock(a, b, c, block.STAINED_GLASS_PURPLE)
if(x1 == x2):
	inc = 1
	if(z1 > z2):
		inc = -1
		print(z1, z2)
	for z in range(z1, z2, inc):
		y = amp * math.sin(1/math.pi * (z - z1)) + baseline
		y = round(y)
		print(x1, y, z)
		a, b, c = coords.mcToPy(x1, y, z)
		mc.setBlock(a, b, c, block.STAINED_GLASS_PURPLE)