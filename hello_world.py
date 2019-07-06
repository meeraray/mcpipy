import sys
sys.path.insert(0, 'C:/Users/ronuk/AppData/Roaming/.minecraft/mcpipy')
from mine import *
import coords
mc = Minecraft()
mc.postToChat("Hello World")
playerPos = mc.player.getPos()
print(playerPos.x)
mc.setBlock(playerPos.x, playerPos.y - 1, playerPos.z, block.STAINED_GLASS_PURPLE)
#print(playerPos.x + " " + playerPos.y + " " + playerPos.z)