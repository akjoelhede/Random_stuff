import os, random, time
from termcolor import colored
from graphics import *
from pygame import mixer

run = True 
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

EXP = 0
EXPMAX = 20
LVL = 0
HP = 50
MANA = 100
MANAMAX = MANA
HPMAX = HP
ATK = 3
MTK = 10
pot = 1
elix = 0
manapot = 1
gold = 0
x = 0
y = 0


mixer.init()
mixer.music.load("music/background.wav")
mixer.music.play(loops = -1, fade_ms=2)

map =  [["plains",	"plains",	"plains",	"plains",	"forest",	"mountain",	"cave"],
	["forest",	"forest",	"forest",	"forest",	"forest",	"hills",	"mountain"],
	["forest",	"fields",	"bridge",	"plains",	"hills",	"forest",	"hills"],
	["plains",	"shop",		"town",		"major",	"plains",	"hills",	"mountain"],
	["plains",	"fields",	"fields",	"plains",	"hills",	"mountain",	"mountain"]]

map1 = [["-", "-", "-", "-", "-", "-", "-"], 
	["-", "-", "-", "-", "-", "-", "-"],
	["-", "-", "-", "-", "-", "-", "-"],
	["-", "-", "-", "-", "-", "-", "-"],
	["-", "-", "-", "-", "-", "-", "-"]]


y_len = len(map)-1
x_len = len(map[0])-1
current_tile = map[y][x]


biom = {

	"plains":{
		"t": "PLAINS",
		"e": True},
	"forest":{
		"t": "WOODS",
		"e": True},
	"fields":{
		"t": "FIELDS",
		"e": False},
	"bridge":{
		"t": "BRIGDE",
		"e": True},
	"town":{
		"t": "TOWN CENTER",
		"e": False},
	"shop":{
		"t": "SHOP",
		"e": False},
	"major":{
		"t": "MAJOR",
		"e": False},
	"cave":{
		"t": "CAVE",
		"e": False},
	"mountain":{
		"t": "MOUNTAIN",
		"e": True},
	"hills":{
		"t": "HILLS",
		"e": True}
}

e_list = ["Goblin", "Orc", "Slime", "Zombie", "Vampire", "Troll"]

mobs = {
	"Goblin": {
		"hp": 15,
		"at": 3,
		"go": 8,
		"xp": 5
	},
	"Orc": {
		"hp": 35,
		"at": 5,
		"go": 18,
		"xp": 10
	},
	"Slime": {
		"hp": 15,
		"at": 2,
		"go": 12,
		"xp": 7
	},
	"Zombie": {
		"hp": 20,
		"at": 4,
		"go": 5,
		"xp": 6
	},
	"Vampire": {
		"hp": 15,
		"at": 2,
		"go": 12,
		"xp": 8
	},
	"Troll": {
		"hp": 30,
		"at": 6,
		"go": 40,
		"xp": 15
	},
	"Dragon": {
		"hp": 100,
		"at": 8,
		"go": 100,
		"xp": 50
	}

}

#######AESTETICS##########
def clear():
	os.system("clear")

def draw():
	print("xX----------------------------Xx")

def artdisplay(text, delay):
	for row in text:
		print(row)
		time.sleep(delay)
##########################

def save():
	list = [

		name,
		str(EXP),
		str(EXPMAX),
		str(LVL),
		str(HP),
		str(ATK),
		str(MANA),
		str(pot),
		str(elix),
		str(manapot),
		str(gold),
		str(x),
		str(y),
		str(key)
	]

	f = open("load.txt", "w")

	for item in list:
		f.write(item + "\n")
	f.close()

######GAINED PLAYER STATS############
def heal(amount):
	global HP
	if HP + amount < HPMAX:
		HP += amount
	else:
		HP = HPMAX
	print(name + "'s HP refilled to " + str(HP) + "!")

def mana_regen(amount):
	global MANA
	if MANA + amount < MANAMAX:
		MANA += amount
	else:
		MANA = MANAMAX
	print(name + "'s mana refilled to " + str(MANA) + "!")

def exp_gain(amount):
	global EXP, LVL, ATK, MTK, EXPMAX

	if EXP + amount < EXPMAX:
		EXP += amount
		print("You have gained " + str(amount) + " exp!")
		
	else:
		LVL += 1
		ATK += 4
		MTK += 2
		EXP = 0
		EXPMAX += 20 
		print("You have leveled up! and gained +4ATK, +2MD")

##########################

#MAIN GAME FIGHT LOOP
def battle():

	global fight, play, run, HP, MANA, pot, elix, manapot, gold, boss, EXP

	if not boss:
		enemy = random.choice(e_list)
		mixer.init()
		mixer.music.load("music/bloodpit.wav")
		mixer.music.play(loops = -1, fade_ms=2)
	else:
		enemy = "Dragon"
		mixer.init()
		mixer.music.load("music/boss.wav")
		mixer.music.play(loops = -1, fade_ms=2)

	hp = mobs[enemy]["hp"]
	hpmax = hp
	atk = mobs[enemy]["at"]
	g = mobs[enemy]["go"]
	exp = mobs[enemy]["xp"]

	while fight:
		clear()
		draw()
		print("Defeat the " + enemy + "!")
		draw()
		print(enemy + "'s HP: " + colored(str(hp), 'red') + "/" + colored(str(hpmax), 'red'))
		draw()
		print(name + "'s MANA: " + colored(str(MANA), 'blue') + "/" + colored(str(MANAMAX), 'blue'))
		print(name + "'s HP: " + colored(str(HP), 'red') + "/" + colored(str(HPMAX), 'red'))
		print("POTIONS: " + str(pot))
		print("ELIXIR: " + str(elix))
		print("MANA POTIONS: " + str(manapot))
		draw()
		print("1 - ATTACK")
		print("2 - USE MAGIC (-30 MANA)")
		if pot > 0:
			print("3 - USE POTION (30HP)")
		if elix > 0:
			print("4 - Use ELIXIR (50HP)")
		if manapot > 0:
			print("5 - Use MANA POTION (50 MANA)")
		draw()

		choice = input("# ")

		if choice == "1":
			hp -= ATK
			print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
			if hp > 0:
				HP -= atk
				print(enemy + " dealt " + str(atk) + " damage to the " + name + ".")
			input("> ")
		
		elif choice == "2":
			if MANA >= 30:
				hp -= MTK
				MANA -= 30
				print(name + " dealt " + str(MTK) + " magic damage to the " + enemy + ".")
				HP -= atk
				print(enemy + " dealt " + str(atk) + " damage to the " + name + ".")
				input("> ")
			else:
				print("Not enough mana...")
			input("> ")

		elif choice == "3":
			if pot > 0:
				pot -= 1
				heal(30)
				HP -= atk
				print(enemy + " dealt " + str(atk) + " damage to the " + name + ".")
				input("> ")
			else:
				print("No potions...")
			input("> ")


		elif choice == "4":
			if elix > 0:
				elix -= 1
				heal(50)
				HP -= atk
				print(enemy + " dealt " + str(atk) + " damage to the " + name + ".")
				input("> ")
			else:
				print("No elixirs...")
			input("> ")

		elif choice == "5":
			if manapot > 0:
				manapot -= 1
				mana_regen(50)
				HP -= atk
				print(enemy + " dealt " + str(atk) + " damage to the " + name + ".")
				input("> ")
			else:
				print("No mana potions...")
			input("> ")

		if HP <= 0:
			print(enemy + " defeated " + name + "...")
			draw()
			fight = False
			play = False
			run = False
			print("GAME OVER")
			mixer.init()
			mixer.music.load("music/music_rip.wav")
			mixer.music.play(loops = -1, fade_ms=2)
			input("> ")
		
		if hp <=0:
			print(name + " defeated " + enemy + "!")
			draw()
			fight = False
			gold += g
			exp_gain(exp)
			print(f"You have found " + str(g) + " gold!")
			if random.randint(0,100) < 30:
				pot += 1
				print("You have found a potion!")
			if random.randint(0,100) < 10:
				elix += 1
				print("You have found an elixir!")

			input("> ")

			if enemy == "Dragon":
				draw()
				print("Congratulations, you have finished the game!")
				mixer.init()
				mixer.music.load("music/ending.wav")
				mixer.music.play(loops = -1, fade_ms=2)
				boss = False
				play = False
				run = False
			input("> ")
			clear()

#########SPECIAL TILES ON MAP##########
def shop():
	global buy, gold, pot, manapot, elix, ATK, MTK

	while buy:
		clear()
		draw()
		print("Welcome to the shop!")
		draw()
		print("GOLD: " + str(gold))
		print("POTIONS: " + str(pot))
		print("ELIXIR: " + str(elix))
		print("ATK: " + str(ATK))
		draw()
		print("1 - BUY POTION (30HP) - 5 GOLD")
		print("2 - BUY ELIXIR (50HP) - 8 GOLD")
		print("3 - BUY MANA POTION (50 MANA) - 12 GOLD")
		draw()
		print("4 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
		print("5 - UPGRADE MAGIC (+4MTK) - 20 GOLD")
		draw()
		print("6 - LEAVE SHOP")

		choice = input("# ")

		if choice == "1":
			if gold >= 5:
				pot += 1
				gold -= 5
				print("You have bought a potion")

			else:
				print("Not enough gold...")
			input("> ")

		elif choice == "2": 
			if gold >= 8:
				elix += 1
				gold -= 8
				print("You have bought an elixir")

			else:
				print("Not enough gold...")
			input("> ")
		elif choice == "3": 
			if gold >= 12:
				manapot += 1
				gold -= 8
				print("You have bought a mana potion")

			else:
				print("Not enough gold...")
			input("> ")
		elif choice == "4":
			if ATK < 10:
				if gold >= 10:
					ATK += 2
					gold -= 10
					print("You have upgraded your weapon")
				else:
					print("Not enough gold...")
			else:
				print("Your weapon cannot be upgraded anymore")
			input("> ")
		elif choice == "5":
			if MTK < 20:
				if gold >= 20:
					MTK += 2
					gold -= 20
					print("You have studied the arts of the arcane magic")
				else:
					print("Not enough gold...")
			else:
				print("Your cannot gain anymore arcane knowledge")
			input("> ")
		elif choice == "6":
			buy = False

def major():
	global speak, key

	while speak:
		clear()
		draw()
		print("Hello there " + name + "!")

		if LVL < 3 and ATK < 10:
			print("You are not strong anough to face the dragon, keep practicing and come back later")
			key = False
		
		else:
			print("You might want to take on that dragon now!, i have marked where the dragons cave is on your map",
			"take this key but be carefull with the beast, good luck")
			map1[0][6] = "C"
			key = True

		draw()
		print("1 - LEAVE")
		draw()

		choice = input("# ")

		if choice == "1":
			speak = False

def cave():
	global boss, key, fight

	while boss:
		clear()
		draw()
		print("Here lies the cave of the dragon. What will you do?")
		draw()

		if key:
			print("1 - USE KEY")
		print("2 - TURN BACK")
		draw()

		choice = input("# ")

		if choice == "1":
			if key:
				fight = True
				battle()
		elif choice == "2":
			boss = False
##########################

#MAIN GAME LOOP 
while run:

	while menu:
		clear()
		artdisplay(logo, 0.1)
		draw()
		print("1. New Game")
		print("2. Load Game")
		print("3. Rules")
		print("4. Quit Game")
		draw()

		mixer.init()
		mixer.music.load("music/intro.wav")
		mixer.music.play(loops = -1, fade_ms=2)

		if rules:
			print("Hello there, here are the rules")
			rules = False
			choice = ""
			input("> ")
		else:
			choice = input("# ")

		if choice == "1":
			clear()
			name = input("# What is your name hero? \n")
			menu = False
			play = True
		elif choice == "2":
			try:
				f = open("load.txt", "r")
				load_list = f.readlines()
				if len(load_list) == 14:
					name = load_list[0][:-1]
					EXP = int(load_list[1][:-1])
					EXPMAX = int(load_list[2][:-1])
					LVL = int(load_list[3][:-1])
					HP = int(load_list[4][:-1])
					ATK = int(load_list[5][:-1])
					MANA = int(load_list[6][:-1])
					pot = int(load_list[7][:-1])
					elix = int(load_list[8][:-1])
					manapot = int(load_list[9][:-1])
					gold = int(load_list[10][:-1])
					x = int(load_list[11][:-1])
					y = int(load_list[12][:-1])
					key = bool(load_list[13][:-1])
					clear()
					print("Welcome back, " + name + "!")
					input("> ")
					menu = False
					play = True
				else:
					print("Corrupt save file")
					input("> ")
			except OSError:
				print("No loadable save file")
				input("> ")

		elif choice == "3":
			clear()
			rules = True
		elif choice == "4":
			quit()

	while play:
		save()
		clear()

		if not standing:
			if biom[map[y][x]]["e"]:
				if random.randint(0,100) <= 30:
					fight = True
					battle()

		if play:

			draw()
			print("LOCATION: " + biom[map[y][x]]["t"])
			draw()
			print("NAME: " + colored(name, 'green'))
			print("Lvl: " + str(LVL))
			print("EXP: " + str(EXP) + "/" + str(EXPMAX))
			print("HP: " + colored(str(HP), 'red') + "/" + colored(str(HPMAX), 'red'))
			print("MANA: " + colored(str(MANA), 'blue') + "/" + colored(str(MANAMAX), 'blue'))
			print("ATK: " + str(ATK))
			print("MD: " + str(MTK))
			print("POTIONS: " + str(pot))
			print("ELIXIRS: " + str(elix))
			print("MANA POTIONS: " + str(manapot))
			print("GOLD: " + colored(str(gold), 'yellow'))
			print("COORDINATES: ", x, y)
			draw()
			print("0 - SAVE & QUIT")
			print("1 - NORTH")
			print("2 - EAST")
			print("3 - SOUTH")
			print("4 - WEST")
			
			if pot > 0:
				print("5 - USE POTION (30HP)")
			if elix > 0:
				print("6 - USE ELIXIR (50HP)")
			if manapot > 0:
				print("7 - USE MANA POTION (30 MANA)")
			if map[y][x] == "shop" or map[y][x] == "major" or map[y][x] == "cave":
				print("8 - ENTER ?")

			draw()

			map1[y][x] = "P"
			map1[2][2] = "B"
			map1[3][2] = "T"
			map1[3][3] = "M"
			map1[3][1] = "S"
		
			print(map1[0], "\n")
			print(map1[1], "\n")
			print(map1[2], "\n")
			print(map1[3], "\n")
			print(map1[4])

			draw()
			dest = input("# ")

			if dest == "0":
				play = False
				menu = True
				save()
				play = False
			elif dest == "1":
				map1[y][x] = "-"
				if y > 0:
					y -= 1
					standing = False
				else:
					y = y_len
					standing = False
			elif dest == "2":
				map1[y][x] = "-"
				if x < x_len:
					x +=1
					standing = False
				else:
					x = 0
					standing = False
			elif dest == "3":
				map1[y][x] = "-"
				if y < y_len:
					y += 1
					standing = False
				else:
					y = 0
					standing = False
			elif dest == "4":
				map1[y][x] = "-"
				if x > 0:
					x -=1
					standing = False
				else:
					x = x_len
					standing = False
			elif dest == "5":
				if pot > 0:
					pot -= 1
					heal(30)
				else:
					print("No potions...")
				input("> ")
				standing = True
			elif dest == "6":
				if elix > 0:
					elix -= 1
					heal(50)
				else:
					print("No elixirs...")
				input("> ")
				standing = True
			elif dest == "7":
				if manapot > 0:
					manapot -= 1
					mana_regen(50)
				else:
					print("No manapotion...")
				input("> ")
				standing = True
			elif dest == "8":
				if map[y][x] == "shop":
					buy = True
					shop()
				if map[y][x] == "major":
					speak = True
					major()
				if map[y][x] == "cave":
					boss = True
					cave()
			else:
				standing = True
			