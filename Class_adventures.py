import numpy as np
import matplotlib.pyplot as plt


#A CLASS DOES NOT TAKE ANY PARAMETERS OR VALUES
class Twoparticles():

	def __init__(self, parameters): # THE __INIT__ FUNCTION DEFINES THE PARAMETERS IN THE CLASS
		self.parameters= parameters

		
	#ALL FUNCTIONS BELOW THIS ARE CALLABLE 

	def pot_run(self,parameters):
		pot = parameters[0]**2 + parameters[1] + parameters[2]
		return pot
	
	def kin_run(self,parameters):
		kin = parameters[1]**2 * parameters[0] -parameters[2]
		return kin

parameters = np.array([2,1,3])

#THIS CALLS THE CLASS AND ASSIGNS IT TO A VARIABLE S. X AND Y ARE GIVEN AS PARAMETERS
s = Twoparticles(parameters=parameters)

#HERE I CALL A FUNCTION WITHIN THE CLASS TO CALCULATE THE POTENTIAL ENERGY
pot = s.pot_run(parameters)

#HERE I CALL ANOTHER FUNCTION WITHIN THE CLASS EASILY
kin = s.kin_run(parameters)

print(pot, kin)