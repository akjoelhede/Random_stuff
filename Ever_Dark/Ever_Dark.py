import time
from graphics import *
import json
#import winsound
from pygame import mixer


#winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
#custom_fig = Figlet(font='doom')

##########################Inventory##########################
weapon = False
coin = 10
potion = False
boat_tools = False
lighthouse_werewolf = True
Health = 20
Sanity = 100
#############################################################

def back():
	global weapon
	global coin
	global potion
	global Sanity
	global Health

	directions = ["Town", "Marsch", "Shore"]
	actions = ["Inspect Knife", "Check pockets", "Whistle", "Choose direction", "Inventory", "Stats"]
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
					if potion == False:
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
						if Sanity > 100:
							Sanity = 100
					else:
						typewriter(["You cannot gain more sanity from this memory"], 0.1)
				elif userinput == "4":
					introscene()
				elif userinput == "5":
					typewriter([f"You have weapon = {weapon}, and {coin} gold coins and potion = {potion}"], 0.1)
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
	directions = ["Beach", "Town"]
	typewriter(["Where would you like to go?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			beach()
		elif userinput == "2":
			town()
		else:
			print("Please enter a valid option")

#########LIGHTHOUSE########
def lighthouse():
	directions = ["Inside", "To the basement"]
	typewriter(["Soon after leaving the shore, you see a lighthouse towering in the distance "], 0.1)

	artdisplay(lighthouse_art, 0.1)

	typewriter(["Where would you like to go?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			if lighthouse_werewolf == False:
				inside_lighthouse()
			else:
				inside_lighthouse_werewolf()
		elif userinput == "2":
			lighthouse_basement()
		else:
			print("Please enter a valid option")

def inside_lighthouse_werewolf():

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
				typewriter(["The werewolf mauls you and begin feasting on your flesh!",
				"Your story ends here traveler"], 0.1)
				typewriter(["GAME OVER!"], 0.1)
				quit()
		elif userinput == "2":
			lighthouse_basement()
		else:
			print("Please enter a valid option")

def inside_lighthouse():

	global boat_tools

	directions = ["Beach", "Shore"]
	typewriter(["You now stand in the middle of a large room of stone and wood",
	"You manage to find a tool belt with all the tools you need to fix the boat"], 0.1)
	
	boat_tools = True

	typewriter(["Where will you go?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			beach()
		elif userinput == "2":
			shore()
		else:
			print("Please enter a valid option")

def lighthouse_basement():

	global weapon

	typewriter(["You use walk around the lighthouse to find a small door in the side of the building. ",
	"The rusty hinges scream in agony as you pull the door open and walk down into the cellar"], 0.1)

	



def boat_broken():
	directions = ["Lighthouse", "Beach"]

	typewriter(["A boat can take you anywhere, but this one seems to be broken....."], 0.1)
	
	artdisplay(boat_broken_art, 0.1)

	typewriter(["Maybe theres is someone with the tools to fix it in the lighthouse?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			lighthouse()
		elif userinput == "2":
			beach()
		else:
			print("Please enter a valid option")

def boat_fixed():
	directions = ["Set sail", "Go back"]

	typewriter(["Using your tools you manage to fix up the boat, ready for adventure"], 0.1)
	
	artdisplay(boat_art, 0.1)

	typewriter(["What might be on the other side of the merciless sea?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			izetun()
		elif userinput == "2":
			beach()
		else:
			print("Please enter a valid option")

def beach():

	global boat_tools
	
	directions = ["Inpect boat", "Go Back"]

	typewriter(["You make your way onto the beach and you feel your boots sink into the sand and the smell of salt on the wind."], 0.1)
	
	typewriter(["What would you like to do ?"], 0.1)

	userinput = ""

	while userinput not in directions:
		print(directions)
		userinput = input()
		if userinput == "1":
			if boat_tools == True:
				boat_fixed()
			else:
				boat_broken()
		elif userinput == "2":
			shore()
		else:
			print("Please enter a valid option")
			

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
	#print(custom_fig.renderText("Rules"))
	typewriter(["Rules"], 0.1)
	time.sleep(1)
	typewriter(["If you have chosen a path and want to go back but can't, you have to restart.",
	"Every decision you make have an impact on how the game plays out, for good or for bad"], 0.1)

	#print(custom_fig.renderText("Mechanics"))
	typewriter(["Mechanics"], 0.1)
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
	mixer.init()
	mixer.music.load("Ever_Dark/music/background.wav")
	mixer.music.play(loops = -1)
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

def main_menu():

	artdisplay(logo, 0.1)

	print("\n")

	actions = ["New game", "Rules and mechanics"]

	userinput = ""

	while userinput not in actions:
		mixer.init()
		mixer.music.load("Ever_Dark/music/intro.wav")
		mixer.music.play(loops = -1, fade_ms=2)

		print(actions)
		userinput = input()
		if userinput == "1":
			introscene()
		elif userinput == "2":
			marsch()
		elif userinput == "3":
			Rules_and_Mechanics()
		else:
			print("Please enter a valid option")

if __name__ == "__main__":
	while True:
		#print(custom_fig.renderText("WELCOME TO EVER DARK"))
		typewriter(["WELCOME TO EVER DARK"], 0.1)
		typewriter(["A choice based story game"], 0.1)
		time.sleep(1)
		typewriter(["Good luck traveler"], 0.1)

		main_menu()