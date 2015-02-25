class = Word(object):
	"""This will hold a bunch of variables that templates will read from to construct 
	descriptions and that Creatures and Rooms will need to construct themselves"""
	def __init__(self, word, plural, wtype=None, subtype=None):
		self.word = word
		self.type = wtype #adjective, noun, mood, nationality, amount, weapon
		self.subtype = subtype
		self.plural = plural
		if word[0].lower() in ['a','e','i','o','u']:
			self.vowelstart = True
		else:
			self.vowelstart = False
