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
blocks = [block.WOOL_LIGHT_BLUE, block.WOOL_PINK, block.WOOL_WHITE, block.WOOL_PINK, block.WOOL_LIGHT_BLUE]
transformation = 0

for trans in range(5):
	if(z1 == z2):
		if(x1 > x2):
			a = x1
			x1 = x2
			x2 = a
			print(x1, x2)
		for x in range(x1, x2):
			y = amp * math.sin(1/math.pi * (x - x1)) + baseline
			y = round(y) + trans
			print(x, y, z1)
			a, b, c = coords.mcToPy(x, y, z1)
			print(blocks[trans])
			mc.setBlock(a, b, c, blocks[trans])
	if(x1 == x2):
		if(z1 > z2):
			a = z1
			z1 = z2
			z2 = a
			print(z1, z2)
		for z in range(z1, z2):
			y = amp * math.sin(1/math.pi * (z - z1)) + baseline
			y = round(y) + trans
			print(x1, y, z)
			a, b, c = coords.mcToPy(x1, y, z)
			print(blocks[trans])
			mc.setBlock(a, b, c, blocks[trans])