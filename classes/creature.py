from cre_templates import *
import random


class Creature(object):
	'''Creatures are the basic inhabitants of the world. They have
	various inherent properties like hit points and damage, and can
	do things like manipulate items, attack each other and level up'''

	def __init__(self, hp=10, dmg=2, speed=5, desc="A nondescript creature",
				 room="The Nether", is_active=False, 
				 looked_at="Sure looks deadly...", gender="neutral", internal="", level = 0):

		self.level = level
		self.internal = internal
		self.gender = gender
		self.active = is_active
		self.description = desc
		self.hp = hp
		self.damage = dmg
		self.inventory = []
		self.speed = speed
		self.looked_at = looked_at
		self.combat_action = "attack"

	def attack(self, cre1):
		cre1.hp += self.damage*-1

	def attack_enemy(self):
		print "placeholder string"

	def make_random(self):
		'''Sets a random description variable, internal, and other features'''

		self.description = ""

		no_mods = random.randint(0,3)
		mod_types = ["mood", "adjective", "nationality", "weapon"]
		mods = []

		for n in range(no_mods):
			choosemod = random.choice(mod_types)
			if choosemod in ['mood','nationality']:
				mod_types.remove(choosemod)
			mods.append(choosemod)

		keywords = []
		for modtype in mods:
			avail_words = []
			for word in wordlist:
				if word.type = modtype:
					avail_words.append(word)
			word = random.choice(avail_words)
			keywords.append(word)

		tempamount = 1
		if len(keywords) < (self.level+3):
			for word in keywords:
				if word.subtype = "candy":
					tempamount *= random.choice([50,75,100])
				else:
					tempamount *= random.choice([1,2,3,5,10])

		for word in wordlist:
			if (word.type = "amount") and (word.subtype = tempamount):
				keywords.append(word)

		template = "amount mood nationality adjective noun weapon"
		templatelist = template.split(" ")

		for word in keywords:


		# self.description = ""

		# if len(mods) < self.level+3:
		# 	if ("gummy" or "gingerbread") in mods:
		# 		amount = random.choice(cre_amount[-4:])
		# 	else: amount = random.choice(cre_amount[:4])
		# else: amount = (1, "a")

		# (number, no_desc) = amount

		# noun = random.choice(cre_noun)
		# self.internal = noun

		# if number > 1: 
		# 	self.gender = "collective"
			
		# 	self.description += no_desc + " of "
		# 	if noun[-3:] == "man":
		# 		noun = noun[:-3] + "men"
		# 		self.internal = "strongmen"
		# 	elif noun == "bunny":
		# 		noun = "bunnies"
		# 		self.internal = noun
		# 	else:
		# 		noun += "s"
		# 		self.internal += "s"

		# list(set(mods))

		# for mod in mods:
		# 	if mod in cre_mood: 
		# 		self.description += mod + ", "

		# for mod in mods:
		# 	if mod in cre_nationality: 
		# 		self.description += mod + ", "

		# for mod in mods:
		# 	if mod in cre_adjective: 
		# 		self.description += mod + ", "

		# self.description = self.description[:-2] + " " + noun

		# weaps = []
		# for mod in mods:
		# 	if mod in cre_weapon: 
		# 		weaps.append(mod)

		# if len(weaps) == 1:
		# 	self.description += ", wielding " + weaps[0]
		# elif len(weaps) >= 1:
		# 	self.description += ", wielding "
		# 	for weap in weaps:
		# 		self.description += weap + " and "
		# 	self.description = self.description[:-5]






		




		# apply modifiers to base creature
		# describe result
		# set description, internal, gender
