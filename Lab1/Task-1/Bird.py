class Bird:
	encode_size = {0: "маленькая", 1: "средняя", 2: "большая"}
	def __init__(self, name, size, color, water, wildRussia, sq = None):
		self.name = name
		self.size = size
		self.brightColor = color
		self.waterfowl = water
		self.wildInRussia = wildRussia
		self.specialQuality = sq

	def __str__(self):
		return self.name