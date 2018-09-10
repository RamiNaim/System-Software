def get_numbers():
	numbers_srt = input("Введите числа через запятую (после запятой пробел, десятичный разделитель - точка, косплексный вид: a+bj):\n")
	print()
	numbers = numbers_srt.split(", ")
	for num in numbers:
		parse_number(num)
		#print( num + " - " + parse_number(num) )

	print("Комплексные: " + list_to_str(comp))
	print("Рациональные: " + list_to_str(rational))
	print("Целые: " + list_to_str(integer))
	print("Натуральные: " + list_to_str(natural))
	print("Четные: " + list_to_str(even))
	print("Нечетные: " + list_to_str(odd))
	print("Простые: " + list_to_str(prime_num))


comp=[]
rational=[]
natural=[]
integer=[]
even=[]
odd=[]
prime_num=[]

def parse_number(n):
	n = complex(n)
	if n.imag != 0:
		#return "комплексное"
		comp.append(n)
		return
	else:
		n = float(n.real)

	if n % 1 != 0:
		#return "рациональное"
		rational.append(n)
		return
	else:
		n = int(n)

	result = ""
	if n <= 0:
		#result += "целое"
		integer.append(n)
	else:
		#result += "натуральное"
		natural.append(n)
		integer.append(n)
		if prime(n):
			#result += ", простое"
			prime_num.append(n)

	if n % 2 == 0:
		#result += ", четное"
		even.append(n)
	else:
		#result += ", нечетное"
		odd.append(n)

	return

def prime(n):
	if n == 1:
		return False

	top_lim = n // 2 + 1
	for den in range(2, top_lim):
		if n % den == 0:
			return False

	return True

def list_to_str(l):
	s = ""
	for elem in l:
		s += str(elem) + ", "
	s = s[0:-2]
	return s



if __name__ == '__main__':
	get_numbers()
