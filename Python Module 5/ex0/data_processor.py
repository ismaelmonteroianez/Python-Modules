from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def __init__(self) -> None:
        self.data: list[str] = []
        self.counter = 0
    """
    We delete de oldest element in the list with pop(0)
    We return the quantity of elements after deleting that one
    Plus the one deleted as str
    """
    def output(self) -> tuple[int, str]:
        if self.data == []:
            raise ValueError("No data available")
        item_to_delete = self.data.pop(0)
        counter = self.counter
        self.counter += 1
        return (counter, item_to_delete)
    """
    We validate with isinstance numbers, floats and
    if is a list, every element in that list and
    return a boolean
    """


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                return True
        return False
    """
    We use inigest to append the new data
    to the old data, if is a list we append
    everything
    """
    def ingest(self, data: int | float | list[int]
               | list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self.data.append(str(x))
            return
        self.data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            if all(isinstance(x, (str)) for x in data):
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self.data.append(x)
            return
        self.data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if "log_level" in data and "log_message" in data:
                if all(isinstance(key, (str)) and isinstance(value, (str))
                       for key, value in data.items()) is True:
                    return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if "log_level" not in item or "log_message" not in item:
                    return False
                if not all(isinstance(key, (str)) and isinstance(value, (str))
                           for key, value in item.items()):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, dict):
            log_entry = f"{data['log_level']}: {data['log_message']}"
            self.data.append(log_entry)
            return
        elif isinstance(data, list):
            for item in data:
                log_entry = f"{item['log_level']}: {item['log_message']}"
                self.data.append(log_entry)
            return


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    numeric_test = NumericProcessor()
    print("Testing Numeric Processor...")
    number = 42
    test_result = numeric_test.validate(number)
    print(f" Trying to validate input '{number}': {test_result}")
    not_number = "Hello"
    test_result_2 = numeric_test.validate(not_number)
    print(f" Trying to validate input '{not_number}': {test_result_2}")
    not_number_2 = "foo"
    print(f" Test invalid ingestion of string '{not_number_2}' "
          "without prior validation:")
    try:
        numeric_test.ingest(not_number_2)
    except ValueError as e:
        print(f" Got exception: {e}")
    array_numbers = [1, 2, 3, 4, 5]
    print(f" Processing data: {array_numbers}")
    numeric_test.ingest(array_numbers)
    print(" Extracting 3 values...")
    for x in range(3):
        test_result_3 = numeric_test.output()
        print(f" Numeric value {test_result_3[0]}: {test_result_3[1]}")
    text_test = TextProcessor()
    print()
    print("Testing Text Processor...")
    not_string = 42
    test_result_4 = text_test.validate(not_string)
    print(f" Trying to validate input '{not_string}': {test_result_4}")
    string_list = ["Hello", "Nexus", "World"]
    print(f" Processing data: {string_list}")
    text_test.ingest(string_list)
    print(" Extracting 1 values...")
    for x in range(1):
        test_result_5 = text_test.output()
        print(f" Text value {x}: {test_result_5[1]}")
    print()
    print("Testing Log Processor...")
    dict_test = LogProcessor()
    not_dict = "Hello"
    test_result_6 = dict_test.validate(not_dict)
    print(f" Trying to validate input '{not_dict}': {test_result_6}")
    logs = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {logs}")
    dict_test.ingest(logs)
    print(" Extracting 2 values...")
    for x in range(2):
        test_result_7 = dict_test.output()
        print(f" Log entry {x}: {test_result_7[1]}")


if __name__ == "__main__":
    main()
