from abc import ABCMeta, abstractmethod

from numerical import Constants

import numpy as np 
from math import sin 
from math import cos
from math import pi

#Main class that serves as a blueprint for all rotation related functions.
#Objects of the Rotation class cannot be created

class Rotation(object):

	__metaclass__ = ABCMeta

	def __init__(self, units = 'rad'):
		self.units = units

	@abstractmethod
	def get_units(self):
		return self.units 

	@abstractmethod
	def set_units(self, units):
		self.units = units




