class Bird:
	encode_size = {0: "маленькая", 1: "средняя", 2: "большая"}
	def __init__(self, name, size, water, wildRussia, sq = None):
		self.name = name
		self.size = size
		self.waterfowl = water
		self.wildInRussia = wildRussia
		self.specialQuality = sq