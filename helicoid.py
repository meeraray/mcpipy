#
# Code by Alexander Pruss and under the MIT license
#

import setup
from mine import *
import sys

def draw_surface(xf,yf,zf,a0,a1,asteps,b0,b1,bsteps,ox,oy,oz,scalex,scaley,scalez,mcblock,mcmeta):

  for i in range(asteps):
     a = (a0 * (asteps-1-i) + a1 * i) / asteps
     for j in range(bsteps):
        b = (b0 * (bsteps-1-j) + b1 * j) / bsteps
        x = xf(a,b)
        y = yf(a,b)
        z = zf(a,b)
#        print a,b,ox+x * scalex, oy+y * scaley, oz+z * scalez
        mc.setBlock(ox+x * scalex, oy+y * scaley, oz+z * scalez, mcblock, mcmeta)

mc = Minecraft()
playerPos = mc.player.getPos()

xformula = lambda a,b: a * cos(b)
yformula = lambda a,b: b
zformula = lambda a,b: a * sin(b)

scale = 15

b = block.WOOL_PINK
m = 0

draw_surface(xformula,yformula,zformula,0,1.,10*scale,0,2*pi,30*scale,playerPos.x,playerPos.y+scale,playerPos.z,scale,scale,scale,b, m)
mc.postToChat("Formula done")
