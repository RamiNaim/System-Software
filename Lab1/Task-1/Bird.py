"""Класс, описывающий птицу"""
"""Каждая птица имеет название(name), размер(size), окрас(brightColor), лог.переменную, отвечающую за водоплавание(waterfowl)"""
"""лог.переменную, отвечающую за обитание в дикой среде России(wildInRussia), и специальный атрибут, необходимый для определения некоторых птиц(sprecialQuality)"""
class Bird:
	def __init__(self, name, size, color, water, wildRussia, sq = None):
		self.name = name
		self.size = size
		self.brightColor = color
		self.waterfowl = water
		self.wildInRussia = wildRussia
		self.specialQuality = sq

	def __str__(self):
		return self.name
