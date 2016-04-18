import pygame as gfx
class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		

	def draw(self, screen, color):
		margin = self.margin
		
		color = (0, 0, 255) if (self.walkable) else (255,0,0)
		
		
		
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
	def setWalk(self, walkable):
		self.walkable = walkable




