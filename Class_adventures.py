import numpy as np
import matplotlib.pyplot as plt


#A CLASS DOES NOT TAKE ANY PARAMETERS OR VALUES
class Twoparticles():

	def __init__(self, x, y): # THE __INIT__ FUNCTION DEFINES THE PARAMETERS IN THE CLASS
		self.x= x
		self.y = y
		
	#ALL FUNCTIONS BELOW THIS ARE CALLABLE 

	def pot_run(self,x,y):
		pot = x**2 + y
		return pot
	
	def kin_run(self,x,y):
		kin = y**2 * x
		return kin


x = np.linspace(2,6)
y = np.linspace(3,7)

#THIS CALLS THE CLASS AND ASSIGNS IT TO A VARIABLE S. X AND Y ARE GIVEN AS PARAMETERS
s = Twoparticles(x=x, y = y)

#HERE I CALL A FUNCTION WITHIN THE CLASS TO CALCULATE THE POTENTIAL ENERGY
pot = s.pot_run(x, y)

#HERE I CALL ANOTHER FUNCTION WITHIN THE CLASS EASILY
kin = s.kin_run(x, y)

print(pot[0], kin[0])