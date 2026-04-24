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
				raise ValueError("Improper numeric data")
		if isinstance(data, list) == True:
			for x in data:
				self.data.append(str(x))
			return
		self.data.append(str(data))


class TextProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, (str)) == True:
			return True
		if isinstance(data, list) == True:
			if all(isinstance(x,(str)) for x in data) == True:
				return True
		return False


	def ingest(self, data: Any) -> None:
		if self.validate(data) == False:
			raise ValueError("Invalid parameter (need str)")
		if isinstance(data, list) == True:
			for x in data:
				self.data.append(x)
			return
		self.data.append(data)


class LogProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, dict) == True:
			if "log_level" in data and "log_message" in data:
				if all(isinstance(key, (str)) and isinstance(value, (str)) for key, value in data.items()) == True:
					return True
		if isinstance(data, list) == True:
			for item in data:
				if not isinstance(item, dict):
					return False
				if "log_level" not in item or "log_message" not in item:
					return False
				if not all(isinstance(key, (str)) and isinstance(value, (str)) for key, value in item.items()):
					return False
			return True				
		return False


	def ingest(self, data: Any) -> None:
		if self.validate(data) == False:
			raise ValueError ("Invalid parameter (need dict)")
		if isinstance(data, dict) == True:
			log_entry = f"{data['log_level']}: {data['log_message']}"
			self.data.append(log_entry)
			return
		elif isinstance(data, list) == True:
			for item in data:
				log_entry = f"{item['log_level']}: {item['log_message']}"
				self.data.append(log_entry)
			return


def main():
	print("=== Code Nexus - Data Processor ===")
	print()
	numeric_test = NumericProcessor()
	print("Testing Numeric Processor...")
	test = 42
	result = numeric_test.validate(test)
	print(f" Trying to validate input '{test}': {result}")
	test = "Hello"
	result = numeric_test.validate(test)
	print(f" Trying to validate input '{test}': {result}")
	test = "foo"
	print(f" Test invalid ingestion of string '{test}' without prior validation:")
	try:
		numeric_test.ingest(test)
	except ValueError as e:
		print(f" Got exception: {e}")
	test = [1, 2, 3, 4, 5]
	print(f" Processing data: {test}")
	numeric_test.ingest(test)
	print("Extracting 3 values...")
	for x in range(3):
		result = numeric_test.output()
		print(f" Numeric value {x}: {result[1]}")
	text_test = TextProcessor()
	print()
	print("Testing Text Processor...")
	test = 42
	result = text_test.validate(test)
	print(f" Trying to validate input '{test}': {result}")
	test = ["Hello", "Nexus", "World"]
	text_test.ingest(test)
	print(" Extracting 1 values...")
	for x in range(1):
		result = text_test.output()
		print(f" Text value {x}: {result[1]}")
	print()
	print("Testing Log Processor...")
	dict_test = LogProcessor()
	test = "Hello"
	result = dict_test.validate(test)
	print(f"Trying to validate input '{test}': {result}")
	test = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
	dict_test.ingest(test)
	print("Extracting 2 values...")
	for x in range(2):
		result = dict_test.output()
		print(f"Log entry {x}: {result[1]}")


	







if __name__ == "__main__":
	main()