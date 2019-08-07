import setup
from mine import *
import time

from coords import mcToPy

mc = Minecraft()

class Sphere:
	def gen_shape(self, blockname=block.WOOL_PINK, size=0):
		if(size == 0):
			size = self.radius
		print("test")
		xCoord = int(self.x)
		yCoord = int(self.y)
		zCoord = int(self.z)
		for x in range(xCoord - size, xCoord + size + 1):
			for y in range(yCoord - size, yCoord + size + 1):
				for z in range(zCoord - size, zCoord + size + 1):
					num = (x - xCoord) ** 2 + (y - yCoord) ** 2 + (z - zCoord) ** 2
					if(num <= size ** 2):
						# mc.setBlock(x, y, z, blockname)
						self.blocks.append([x, y, z])
	
	def render(self, blockname=block.WOOL_PINK):
		for coord in self.blocks:
			mc.setBlock(coord[0], coord[1], coord[2], blockname)
	
	def __init__(self, x, y, z, radius=5):
		self.x = x
		self.y = y
		self.z = z
		self.radius = radius
		
		self.xDir = 0
		self.yDir = 0
		self.zDir = 0
		self.blocks = []
		
		self.gen_shape()
	
	def move(self):
		self.render(block.AIR)
		self.x = self.x + self.xDir
		self.y = self.y + self.yDir
		self.z = self.z + self.zDir
		for coord in self.blocks:
			coord[0] = coord[0] + self.xDir
			coord[1] = coord[1] + self.yDir
			coord[2] = coord[2] + self.zDir
		self.render()

x, y, z = mcToPy(242, 64,  807)
test_sphere = Sphere(x, y, z, 10)
test_sphere.gen_shape()
test_sphere.draw()
test_sphere.xDir = 1;
test_sphere.yDir = 1;
test_sphere.zDir = 1;


def test():
	while True:
		test_sphere.move()
		time.sleep(1)
test()