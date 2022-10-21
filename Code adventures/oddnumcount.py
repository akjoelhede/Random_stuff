
def countOdds(low: int, high: int):
	num_store = []
	for num in range(low, high + 1):
		if num % 2 != 0:
			num_store.append(num)
	print(len(num_store))
print(countOdds(3, 7))