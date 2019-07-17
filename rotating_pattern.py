#cycles through a pattern of blocks defined with string array
#choose one of the two patterns below or create your own
#uncomment last line to run

import setup
from mine import *
import time

mc = Minecraft()
#mc.postToChat("test")

#Takes 2-dimensional array of strings, tuple that represents where player is standing, array of blocks to use
#in MC, face north so -x to left, +x to right, facing in -z
def drawXZPatternFromStrings(str_array, center, blocks):
	playerPos = mc.player.getPos()
	x = playerPos.x
	y = playerPos.y
	z = playerPos.z
	y = y - 1
	for row in range(0, len(str_array)):
		for col in range(0, len(str_array[row])):
			#print(str_array[row][col])
			char = str_array[row][col]
			if(char != "-"):
				relX = col - center[0]
				relZ = row - center[1]
				#print(x + relX, y, z + relZ)
				mc.setBlock(x + relX, y, z + relZ, blocks[int(char)])

#shifts block list once
def shift(blocks):
	last = blocks.pop()
	blocks.insert(0, last)
	return blocks

#cycles through pattern, default of 1fps
def cycle(pattern, center, blocks, interval=1):
	while True:
		drawXZPatternFromStrings(pattern, center, blocks)
		blocks = shift(blocks)
		time.sleep(interval)

cross_pattern = [
"----4----", 
"---434---", 
"--43234--", 
"-4321234-", 
"432101234",
"-4321234-", 
"--43234--", 
"---434---",
"----4----"
]
cross_center = (4, 4)
cross_blocks = [block.STAINED_GLASS_LIGHT_BLUE, block.STAINED_GLASS_PINK, block.STAINED_GLASS_WHITE, block.STAINED_GLASS_PINK, block.STAINED_GLASS_LIGHT_BLUE]


square_pattern = [
"444444444",
"433333334",
"432222234",
"432111234",
"432101234",
"432111234",
"432222234",
"433333334",
"444444444"
]
square_center = (4, 4)
square_blocks = [block.STAINED_GLASS_LIGHT_BLUE, block.STAINED_GLASS_PINK, block.STAINED_GLASS_WHITE, block.STAINED_GLASS_PINK, block.STAINED_GLASS_LIGHT_BLUE]


#cycle(square_pattern, square_center, square_blocks)