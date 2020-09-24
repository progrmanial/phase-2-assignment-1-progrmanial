## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	numbers = x.split("/")
	
	if numbers[0] == "0": return "0"
	if numbers[1] == "0": return "Undefined"

	if (int(numbers[0]) < 0 and int(numbers[1]) < 0) or (int(numbers[1]) < 0 and int(numbers[0]) > 0):
		numbers = [-1 * int(x) for x in numbers]
	
	factors_of_numerator = set(factors(numbers[0]))
	factors_of_denominator = set(factors(numbers[1]))

	common_factor = factors_of_numerator & factors_of_denominator

	if common_factor:
		highest_common_factor = max(common_factor)

	if highest_common_factor:
		return "{}/{}".format(int(numbers[0]) // highest_common_factor, int(numbers[1]) // highest_common_factor )

	return "{}/{}".format(numbers[0], numbers[1])



def factors(x):
	num = int(x)
	mid = num // 2
	factors = []
	if num < 0:
		i = -1
		while i >= num:
			if not num % i:
				factors.append(-i)
			i -= 1
	elif num > 0:
		i = 1
		while i <= num:
			if not num % i:
				factors.append(i)
			i += 1
	return factors
