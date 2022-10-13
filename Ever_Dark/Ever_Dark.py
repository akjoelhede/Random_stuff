from lib2to3.pytree import type_repr
from threading import local
import time
import os
import sys
from pyfiglet import Figlet

custom_fig = Figlet(font='doom')

##########################Inventory##########################
weapons = False
coin = 10
potions = False

##########################stats##############################
Health = 20
Sanity = 100

#############################################################

def typewriter(text, delay):
	for row in text:
		for char in row:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(delay)
		print()
		time.sleep(1)
		os.system('clear')

def artdisplay(text, delay):
	for row in text:
		print(row)
		time.sleep(delay)
		


def back():
	global weapon
	global coin
	global potion
	global Sanity
	global Health

	directions = ["Town", "Marsch", "Shore"]
	actions = ["Inspect Knife", "Check pockets", "Whissle", "Choose direction", "Inventory", "Stats"]
	choice = ["directions", "actions"]

	typewriter(["You turn back, but all of a sudden the world begins spinning around you. You open your eyes and stare at the crossroads once again"], 0.1)
	typewriter(["You suddenly feel a heavy obejct in your hand, a knife"], 0.1)
	typewriter(["What will you do"], 0.1)
	time.sleep(3)

	weapon = True

	
	userinput = ""

	while userinput not in choice:
		print(choice)
		userinput = input()

		if userinput == "1":

			while userinput not in directions:
				print(directions)
				userinput = input()
				if userinput == "1":
					town()
				elif userinput == "2":
					marsch()
				elif userinput == "3":
					shore()
				else:
					print("Please enter a valid option")

		elif userinput == "2":
			while userinput not in actions:
				print(actions)
				
				userinput = input()
				if userinput == "1":
					typewriter(["You notice strange carvings on the knife, they look old and not of this land."], 0.1)
				elif userinput == "2":
					if potions == False:
						typewriter(["You a vial of mysterious fluid. Maybe it can be helpful along the way?."], 0.1)
						potion = True
					else:
						typewriter(["There is no more to find in your pockets"], 0.1)
				elif userinput == "3":
					typewriter(["The wind dies as the sound leaves your lips and a raven lands on the rotten sign, digging its talons into the soft wood"], 0.1)
					typewriter(["You recall a melody and begin humming, 'The raven is a wicked bird, with wings as black as sin'."], 0.1)
					
					if Sanity < 100:
						typewriter(["You gained 5 sanity points"], 0.1)
						Sanity += 5
					else:
						typewriter(["You cannot gain more sanity from this memory"], 0.1)
				elif userinput == "4":
					introscene()
				elif userinput == "5":
					typewriter([f"You have weapons = {weapons}, and {coin} gold coins and {potions} potions"], 0.1)
				elif userinput == "6":
					if Health or Sanity > 10:
						typewriter([f'You have {Health} HP and feel good.'], 0.1)
						typewriter([f'You have {Sanity} Sanity points and your mind is calm'], 0.1)
					else:
						typewriter([f'You may want to rest for a bit to regain health and sanity.'], 0.1)

				else:
					print("Please enter a valid option")

		else:
			print("Please enter a valid option")
 
##########################EAST###################################

def marsch():
	directions = ["Village", "Mountains", "Town"]
	typewriter(["Where would you like to go?"], 0.1)
	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			village()
		elif userinput == "2":
			mountains()
		elif userinput == "3":
			town()

		else:
			print("Please enter a valid option")
			
##########################WEST###################################

def shore():
	directions = ["Lighthouse", "Beach", "Boat", "Town"]
	typewriter(["Where would you like to go?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			lighthouse()
		elif userinput == "2":
			beach()
		elif userinput == "3":
			boat()
		elif userinput == "4":
			town()
		else:
			print("Please enter a valid option")

#########LIGHTHOUSE########
def lighthouse():
	directions = ["Inside", "To the basement"]
	typewriter(["Soon after leaving the shore, you see a lighthouse towering in the distance "], 0.1)

	artdisplay(
	["┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼.(▓)",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███████████",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒▒░░▒░░▒",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒░░▒▒░░▒",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒▒░░▒░░▒",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███████████",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████",
	"┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████",
	"┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████",
	"┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████",
	"┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████",
	"┼┼┼┼┼┼┼┼┼┼┼┼█▒▒▒█████▒▒▒█",
	"┼┼┼┼┼┼┼┼┼┼┼┼█▒▒▒█████▒▒▒█",
	"┼┼┼┼┼┼┼┼┼█┼┼█▒▒▒█████▒▒▒█",
	"┼┼┼██████▒█████████████████",
	"┼┼┼█████▒▒▒████████████████",
	"┼┼┼████▒▒▒▒▒███████████████",
	"┼┼┼███▒▒▒▒▒▒▒██████████████",
	"┼┼┼██▒▒▒▒▒▒▒▒▒█████████████",
	"┼┼┼█▒▒▒▒███▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█",
	"┼┼┼██▒▒█████▒▒██▒▒▒████▒▒██",
	"┼┼┼█▒▒▒█████▒▒▒█▒▒▒█▒▒█▒▒▒█",
	"┼┼┼██▒▒█████▒▒██▒▒▒████▒▒██",
	"┼┼┼█▒▒▒█████▒▒▒█▒▒▒▒▒▒▒▒▒▒█",
	"┼┼┼████████████████████████"
	],0.1)

	typewriter(["Where would you like to go?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			inside_lighhouse()
		if userinput == "2":
			lighthouse_basement()

def inside_lighthouse():

	global Health
	global Sanity

	actions = ["Proceed", "Go to the basement"]
	typewriter(["You look closer at the door, it almost look like it was broken down from the outside, but you cannot be sure"], 0.1)

	userinput = ""

	while userinput not in actions:
		print(actions)
		userinput = input()
		if userinput == "1":
			typewriter(["Walking over the broken door and into the lighthouse, you hear a growl!"], 0.1)
			if weapon == True:
				typewriter(["A lump of fur attacks you from the right and you feel a sharp pain in your leg",
				"fortunately you manage to thrust your knife forward and killing the werewolf!"], 0.1)
				typewriter(["You loose 3 HP and 5 sanity "], 0.1)
				Health -= 3
				Sanity -= 5
				inside_lighthouse()
			else: 
				typewriter(["You manage to bolt out of the door without a scratch"], 0.1)
				inside_lighthouse()
		if userinput == "2":
			lighthouse_basement()

def lighthouse_basement():
	typewriter(["You make your way through the door to the lighthouse "], 0.1)


def boat():

	typewriter(["A boat can take you anywhere, but this one seems to be broken....."], 0.1)
	
	artdisplay(
	[
	"_____________¶¶¶¶¶¶¶¶¶¶¶¶¶",
	"_____________¶¶___________¶¶",
	"______________¶____________¶",
	"______________¶_____________¶",
	"_______________¶____________¶",
	"_______________¶____________¶_¶¶",
	"_______________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶",
	"_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶",
	"_____¶____________¶¶_____________¶¶____¶",
	"_____¶¶____________¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶",
	"______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶",
	"______¶¶_____¶¶___________¶______________¶¶",
	"_______¶______¶____________¶______________¶",
	"_______¶______¶¶___________¶_____________¶¶",
	"_______¶_______¶___________¶_____________¶¶",
	"______¶¶_______¶___________¶¶____________¶"
	"______¶¶¶¶¶¶¶¶¶¶¶__________¶¶___________¶¶",
	"___________¶_¶_¶¶________¶¶¶_____¶¶¶¶¶¶¶¶_____¶¶¶",
	"___________¶_¶_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_______¶¶¶¶¶__¶¶",
	"¶¶¶¶¶¶_____¶_¶______¶¶_¶_______¶_¶¶¶¶¶¶¶¶¶___¶¶¶¶¶",
	"¶¶___¶¶¶¶¶¶¶¶¶______¶¶_¶____¶¶¶¶¶¶¶________¶¶",
	"__¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶______¶",
	"____¶____________________________¶¶_¶____¶",
	"_____¶_____¶¶¶_____¶¶_____¶¶¶_____¶¶¶___¶¶",
	"______¶___¶¶_¶¶___¶¶_¶____¶_¶¶__________¶",
	"______¶¶____¶¶_____¶¶¶_____¶¶__________¶¶",
	"_______¶¶_____________________________¶¶",
	"________¶¶___________________________¶¶",
	"_________¶¶________________________¶¶¶",
	"___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶"
	], 0.01)

	typewriter(["Maybe theres is someone in the lighthouse?"], 0.1)


##########################NORTH###################################


def town():
	directions = ["Square", "Blacksmith", "Tavern", "Wathctower", "Shore", "Marsch"]
	typewriter(["Where would you like to go?"], 0.1)
	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			square()
		elif userinput == "2":
			blacksmith()
		elif userinput == "3":
			tavern()
		elif userinput == "4":
			watchtower()
		elif userinput == "5":
			shore()
		elif userinput == "6":
			marsch()
		else:
			print("Please enter a valid option")


########################RULES AND MECHANICS############################

def Rules_and_Mechanics():
	choice = ["Begin"]
	print(custom_fig.renderText("Rules"))
	time.sleep(1)
	typewriter(["If you have chosen a path and want to go back but can't, you have to restart.",
	 "Every decision you make have an impact on how the game plays out, for good or for bad"], 0.1)

	print(custom_fig.renderText("Mechanics"))
	time.sleep(1)
	typewriter(["As of this version there is a health mechanic, you start with 20 HP and loose the game if this number reach zero.",
	"Health can be regained with potions, food or sleep in towns",
	"The other mechanic is sanity which is an indicator of how much your mind have dissolved into madness, i.e. a higher value is better",
	"The starting sanity value for this is 100 and can be gained through triggering nostalgic memories with certain actions in each scenario.",
	"Sanity is lost when you tense situations arise and will be indicated.",
	"When a certain low sanity score is reached the events of the actions you take will alter the game."], 0.1)

	typewriter(["Are you ready to begin?"], 0.1)

	userinput = ""
	while userinput not in choice:
		print(choice)
		userinput = input()
		if userinput == "1":
			introscene()
		else:
			print("Please choose a valid option")


def introscene():
	directions = ["Town", "Marsch", "Shore", "Back"]
	typewriter(["After days of wandering around the roads of Kalar'hyn with a feeling of something missing from your mind, you find yourself at a crossroads"], 0.1)
	typewriter(["An old rotten sign roughly indicates where each path leads you"], 0.1)
	typewriter(["Where would you like to go"], 0.1)
	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			town()
		elif userinput == "2":
			marsch()
		elif userinput == "3":
			shore()
		elif userinput == "4":
			back()
		else:
			print("Please enter a valid option")


if __name__ == "__main__":
	while True:
		print(custom_fig.renderText("WELCOME TO EVER DARK"))
		typewriter(["A choice based story game"], 0.1)
		time.sleep(1)
		typewriter(["Venture deep into the marschlands or the deep mines below to the mountains"], 0.1)
		time.sleep(1)
		typewriter(["The choice is yours, but remember sometimes you can't change the past"], 0.1)
		time.sleep(1)
		typewriter(["Good luck traveler"], 0.1)

		choice = ["Rules and Mechanics","Skip"]

		userinput = ""

		while userinput not in choice:
			print(choice)
			userinput = input()
			if userinput == "1":
				Rules_and_Mechanics()
			elif userinput == "2":
				introscene()
			else:
				typewriter("Please enter a valid option", 0.1)