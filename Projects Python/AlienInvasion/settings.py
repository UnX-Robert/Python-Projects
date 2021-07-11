import pygame

class Settings:
	''' A class to stole all settings for Alien Invasion '''

	def __init__(self):
		'''Initialize the game's static settings.'''
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (0,255,0)
		self.bg_image = pygame.image.load('images/bg.bmp')

		# ship settings
		self.ship_speed_factor = 1.5
		self.ships_limit = 3

		# bullet settings
		self.bullet_speed_factor = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_image = pygame.image.load('images/bullet.bmp')
		self.bullets_allowed = 10

		# Aliens settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.chickens = ['BigChicken.bmp', 'c2.bmp', 'l.bmp', 'Militarychicken.bmp']
		
		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		'''Initialize settings that change throught the game'''
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction if 1 right - 1 left
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50 

	def increase_speed(self):
		'''Increase speed settings and alien point values'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)



