from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
	@abstractmethod
	def validate(self, data: Any) -> bool:
		pass

	@abstractmethod
	def ingest(self, data: Any) -> None:
		pass

	def __init__(self):
		self.data = []
	"""
	We delete de oldest element in the list with pop(0)
	We return the quantity of elements after deleting that one
	Plus the one deleted as str
	"""
	def output(self) -> tuple[int, str]:
		if self.data == []:
			raise ValueError("No data available")
		item_to_delete = self.data.pop(0)
		return (len(self.data), item_to_delete)
	"""
	We validate with isinstance numbers, floats and
	if is a list, every element in that list and
	return a boolean
	"""
class NumericProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, (int, float)) == True:
			return True
		if isinstance(data, list) == True:
			if all(isinstance(x, (int, float)) for x in data) == True:
				return True
		return False
	"""
	We use inigest to append the new data 
	to the old data, if is a list we append
	everything
	"""
	def ingest(self, data: Any) -> None:
		if self.validate(data) == False:
				raise ValueError("Invalid parameter")
		if isinstance(data, list) == True:
			for x in data:
				self.data.append(str(x))
			return
		self.data.append(str(data))


class TextProcessor(DataProcessor):
	pass

class LogProcessor(DataProcessor):
	pass

