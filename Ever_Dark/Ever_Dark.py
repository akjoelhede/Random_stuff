import time

weapon = False



def introscene():
	directions = ["Town", "Marsch", "Shore", "Back"]
	print("After days of wandering around the roads of Kalar'hyn with a feeling of something missing from your mind, you find yourself at a crossroads")
	print("An old rotten sign roughly indicates where each path leads you")
	print("Where would you like to go?")
	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()

		if userinput == "Town":
			town()
		elif userinput == "Marsch":
			marsch()
		elif userinput == "Shore":
			shore()
		elif userinput == "Back":
			confusion()
		else:
			print("Please enter a valid option")


if __name__ == "__main__":
	while True:
		print("WELCOME TO EVER_DARK")
		print("A choice based story game")
		time.sleep(5)
		print("Venture deep into the marschlands or the deep mines below to the mountains")
		time.sleep(5)
		print("The choice is yours, but remember sometimes you can't change the past")
		time.sleep(5)
		print("Good luck traveler")

		introscene()