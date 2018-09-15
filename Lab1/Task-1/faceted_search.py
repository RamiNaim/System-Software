from Bird import Bird
from copy import deepcopy

def start():
	init = []

	# Заполняем лист init разными птицами (16 штук) с уникальной комбинацией атрибутов
	eagle = Bird("Орел", size="средняя", color="не яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России", sq="является символом Америки")
	init.append(eagle)

	turkey = Bird("Индейка", size="средняя", color="не яркая", water="неводоплавающая", wildRussia="не встречается в дикой природе России")
	init.append(turkey)

	peacock = Bird("Павлин", size="большая", color="яркая", water="неводоплавающая", wildRussia="не встречается в дикой природе России", sq="обладает очень красивым хвостом")
	init.append(peacock)

	canary = Bird("Канарейка", size="маленькая", color="яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России", sq="чувствительна к запаху газа")
	init.append(canary)

	cock = Bird("Петух", size="средняя", color="яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России")
	init.append(cock)

	sparrow = Bird("Воробей", size="маленькая", color="не яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России")
	init.append(sparrow)

	duck = Bird("Утка", size="средняя", color="не яркая", water="водоплавающая", wildRussia="встречается в дикой природе России")
	init.append(duck)

	ostrich = Bird("Страус", size="большая", color="не яркая", water="неводоплавающая", wildRussia="не встречается в дикой природе России")
	init.append(ostrich)

	swan = Bird("Лебедь", size="большая", color="не яркая", water="водоплавающая", wildRussia="встречается в дикой природе России")
	init.append(swan)

	parrot = Bird("Попугай Ара", size="большая", color="яркая", water="неводоплавающая", wildRussia="не встречается в дикой природе России", sq="разговаривает")
	init.append(parrot)

	penguin = Bird("Пингвин", size="большая", color="не яркая", water="водоплавающая", wildRussia="не встречается в дикой природе России")
	init.append(penguin)

	woodpecker = Bird("Дятел", size="средняя", color="не яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России", sq="делает дупло?")
	init.append(woodpecker)

	cuckoo = Bird("Кукушка", size="средняя", color="не яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России", sq="оставляет своих птенцов")
	init.append(cuckoo)

	flamingo = Bird("Фламинго", size="большая", color="яркая", water="водоплавающая", wildRussia="не встречается в дикой природе России")
	init.append(flamingo)

	colibri = Bird("Калибри", size="маленькая", color="яркая", water="неводоплавающая", wildRussia="не встречается в дикой природе России", sq="может летать назад")
	init.append(colibri)

	bullfinch = Bird("Снегирь", size="маленькая", color="яркая", water="неводоплавающая", wildRussia="встречается в дикой природе России", sq="любит кушать рябину зимой")
	init.append(bullfinch)


	facered_search(deepcopy(init))



def facered_search(init_list):
	# Счетчик, который показывает, какой атрибут мы определяем
	number_of_attributes = 0

	while len(init_list) != 1:

		possible_attributes = []

		# Фильтруем по размеру
		if number_of_attributes == 0:

			# заполняем лист possible_attributes возможными значениями параметра
			for bird in init_list:
				if bird.size not in possible_attributes:
					possible_attributes.append(bird.size)

			# задаем пользователю вопрос до тех пор, пока не останется один возможный атрибут или пользователь ответит Да
			for i in range( len(possible_attributes) - 1 ):
				print( "Ваша птица " + possible_attributes[i] + "?" )
				user_answer = input()
				if user_answer == "Да":
					index = 0
					# Оставляем в possible_attributes то значение, которое выбрал пользователь
					for _ in range(0, len(init_list) ):
						if init_list[index].size != possible_attributes[i]:
							init_list.pop(index)
							# Если удалили один элемент, уменьшаем индекс на 1
							index -= 1
						index += 1
					break
				else: 
					possible_attributes.pop(i)

			# если остается одно возможное значение, удаляем из init_list все неподходящие значения
			if len( possible_attributes ) == 1:
				print("Тогда ваша птица " + possible_attributes[0])
				index = 0
				for _ in range(0, len(init_list) ):
					if init_list[index].size != possible_attributes[0]:
						init_list.pop(index)
						index -= 1
					index += 1
					if index == len( init_list ):
						break

		# Аналогично проверяем окрас
		elif number_of_attributes == 1:
			for bird in init_list:
				if bird.brightColor not in possible_attributes:
					possible_attributes.append(bird.brightColor)

			for i in range( len(possible_attributes) - 1 ):
				print( "Ваша птица " + possible_attributes[i] + "?" )
				user_answer = input()
				if user_answer == "Да":
					index = 0
					for _ in range(0, len(init_list) ):
						if init_list[index].brightColor != possible_attributes[i]:
							init_list.pop(index)
							index -= 1
						index += 1
						if index == len( init_list ):
							break

					break
				else: 
					possible_attributes.pop(i)

			if len( possible_attributes ) == 1:
				index = 0
				for _ in range(0, len(init_list) ):
					if init_list[index].brightColor != possible_attributes[0]:
						init_list.pop(index)
						index -= 1
					index += 1
					if index == len( init_list ):
						break

		# проверяем, загаданная птица поавает в воде или нет
		elif number_of_attributes == 2:
			for bird in init_list:
				if bird.waterfowl not in possible_attributes:
					possible_attributes.append(bird.waterfowl)

			for i in range( len(possible_attributes) - 1 ):
				print( "Ваша птица " + possible_attributes[i] + "?" )
				user_answer = input()
				if user_answer == "Да":
					index = 0
					for _ in range(0, len(init_list) ):
						if init_list[index].waterfowl != possible_attributes[i]:
							init_list.pop(index)
							index -= 1
						index += 1
						if index == len( init_list ):
							break

					break
				else: 
					possible_attributes.pop(i)

			if len( possible_attributes ) == 1:
				index = 0
				for _ in range(0, len(init_list) ):
					if init_list[index].waterfowl != possible_attributes[0]:
						init_list.pop(index)
						index -= 1
					index += 1
					if index == len( init_list ):
						break

		# Проверяем, встречается ли эта птица в дикой природе России
		elif number_of_attributes == 3:
			for bird in init_list:
				if bird.wildInRussia not in possible_attributes:
					possible_attributes.append(bird.wildInRussia)

			for i in range( len(possible_attributes) - 1 ):
				print( "Ваша птица " + possible_attributes[i] + "?" )
				user_answer = input()
				if user_answer == "Да":
					index = 0
					for _ in range(0, len(init_list) ):
						if init_list[index].wildInRussia != possible_attributes[i]:
							init_list.pop(index)
							index -= 1
						index += 1
						if index == len( init_list ):
							break

					break
				else: 
					possible_attributes.pop(i)

			if len( possible_attributes ) == 1:
				index = 0
				for _ in range(0, len(init_list) ):
					if init_list[index].wildInRussia != possible_attributes[0]:
						init_list.pop(index)
						index -= 1
					index += 1
					if index == len( init_list ):
						break

		# если предыдущих действий не хватило для определения одной птицы, задаем спец. вопрос (Bird.specialQuality)
		elif number_of_attributes == 4:

			for bird in init_list:
				if bird.specialQuality not in possible_attributes:
					possible_attributes.append(bird.specialQuality)

			for i in range( len(possible_attributes) - 1 ):
				print( "Ваша птица " + possible_attributes[i] + "?" )
				user_answer = input()
				if user_answer == "Да":
					index = 0
					for _ in range(0, len(init_list) ):
						if init_list[index].specialQuality != possible_attributes[i]:
							init_list.pop(index)
							index -= 1
						index += 1
						if index == len( init_list ):
							break

					break
				else: 
					possible_attributes.pop(i)

			if len( possible_attributes ) == 1:
				index = 0
				for _ in range(0, len(init_list) ):
					if init_list[index].specialQuality != possible_attributes[0]:
						init_list.pop(index)
						index -= 1
					index += 1
					if index == len( init_list ):
						break


		number_of_attributes += 1

	# Выводим отфильтрованный список. в котором находится один элемент
	print( "Под данные параметры подходит одна птица: " + str(init_list[0]) )


if __name__ == '__main__':
	start()
