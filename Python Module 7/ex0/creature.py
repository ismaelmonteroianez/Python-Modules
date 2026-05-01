from abc import ABC, abstractmethod
import typing


class Creature(ABC):
	def __init__(self, name: str, creature_type: str):
		self.name = name
		self.creature_type = creature_type
	
	@abstractmethod
	def attack(self) -> str:
		pass

	def describe(self):
		return(f"{self.name} is a {self.creature_type} Creature")


class Flameling(Creature):
	def attack(self) -> str:
		return(f"{self.name} uses Ember!")


class Pyrodon(Creature):
	def attack(self) -> str:
		return(f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
	def attack(self) -> str:
		return(f"{self.name} uses Water Gun!")


class Torragon(Creature):
	def attack(self) -> str:
		return(f"{self.name} uses Hydro Pump!")


class CreatureFactory(ABC):
	@abstractmethod
	def create_base(self) -> object:
		pass
	
	@abstractmethod
	def create_evolved(self) -> object:
		pass

class FlameFactory(CreatureFactory):
	def create_base(self):
		return Flameling("Flameling", "Fire type")
	
	def create_evolved(self):
		return Pyrodon("Pyrodon", "Fire type")
	

class AquaFactory(CreatureFactory):
	
	def create_base(self):
		return Aquabub("Aquabub", "Water type")
	
	def create_evolved(self):
		return Torragon("Torragon", "Water type")

