import pygame

import sys
 
from settings import Settings
 	
from ship import Ship 
class AlienInvasion:
"""Overall class to manage game assets and behavior."""
 
 	def __init__(self):
"""Initialize the game, and create game resources."""
	pygame.init()
 
	self.screen = pygame.display.set_mode((1200, 800))
 	pygame.display.set_caption("Alien Invasion")
 
 	def run_game(self):
"""Start the main loop for the game."""
		while True:
 # Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
 					sys.exit()
 
 # Make the most recently drawn screen visible.
			pygame.display.flip()
 
		if __name__ == '__main__':
 # Make a game instance, and run the game.
 
 		def __init__(self):
	pygame.display.set_caption("Alien Invasion")
 
 # Set the background color.
	self.bg_color = (230, 230, 230)
 
		def run_game(self):
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				sys.exit()
 
 # Redraw the screen during each pass through the loop.
 		self.screen.fill(self.bg_color)
 
 # Make the most recently drawn screen visible.
 		pygame.display.flip()
 
 
class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 
 	def __init__(self):
 		pygame.display.set_caption("Alien Invasion")
 
		self.ship = Ship(self)
 
 	def run_game(self):
# Redraw the screen during each pass through the loop.
 		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
 
# Make the most recently drawn screen visible.
		pygame.display.flip()
		
def run_game(self):
 """Start the main loop for the game."""
 	while True:
		self._check_events()
 
 # Redraw the screen during each pass through the loop.
 
	def _check_events(self):
 """Respond to keypresses and mouse events."""
 		for event in pygame.event.get():
 		if event.type == pygame.QUIT:
	sys.exit()
ai = AlienInvasion()
ai.run_game()
