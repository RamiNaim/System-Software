"""Функция просит пользователя ввести числа, затем разделяет строку на отдельные числа"""
def get_numbers():
	numbers_srt = input("Введите числа через запятую (после запятой пробел, десятичный разделитель - точка, косплексный вид: a+bj):\n")
	print()

	"""Разделяем строку на одельны числа"""
	numbers = numbers_srt.split(", ")
	for num in numbers:
		"""Передаем каждое число в виде строки в функцию, которая определяет принадлежность числа к определенной группе"""
		parse_number(num)

	"""Вывод результата"""
	print("Комплексные: " + list_to_str(comp))
	print("Рациональные: " + list_to_str(rational))
	print("Целые: " + list_to_str(integer))
	print("Натуральные: " + list_to_str(natural))
	print("Четные: " + list_to_str(even))
	print("Нечетные: " + list_to_str(odd))
	print("Простые: " + list_to_str(prime_num))

"""Создаем пустые массивы(list) для каждой из групп"""
comp=[]
rational=[]
natural=[]
integer=[]
even=[]
odd=[]
prime_num=[]

"""Функция принимает число в виде строки, и помещает число в соответствующую группу"""
def parse_number(n):
	n = complex(n)
	if n.imag != 0:
		comp.append(n)
		"""Дальше функция не выполняется"""
		return
	else:
		n = float(n.real)

	if n % 1 != 0:
		rational.append(n)
		return
	else:
		n = int(n)

	if n <= 0:
		integer.append(n)
	else:
		integer.append(n)
		natural.append(n)
		"""Если число натуральное, то необходимо проверить его на простоту"""
		if prime(n):
			prime_num.append(n)

	"""Проверка на четность"""
	if n % 2 == 0:
		even.append(n)
	else:
		odd.append(n)

	return

"""Функция принимает в виде аргумента число и возвращает True, если число простое, иначе - False"""
def prime(n):
	"""Если передана едининца - возвращаем 1"""
	if n == 1:
		return False

		"""Достаточно проверить, являются ли все числа от 2 до n/2 (округление в большую сторону), делителями числа n"""
	top_lim = n // 2 + 1
	for den in range(2, top_lim):
		if n % den == 0:
			return False

	return True

"""Функция переводит list в строку"""
def list_to_str(l):
	s = ""
	for elem in l:
		s += str(elem) + ", "
	s = s[0:-2]
	return s



if __name__ == '__main__':
	get_numbers()
