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


class DataStream():
    def __init__(self) -> None:
        self.processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processor_list.append(proc)
        else:
            print("Improper data processor")

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processor_list:
                if processor.validate(element):
                    processed = True
                    processor.ingest(element)
            if not processed:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        pass


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    first_batch = ['Hello world', [3.14, -1, 2.71], 
                   [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
                    {'log_level': 'INFO', 'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
    data_stream = DataStream()
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.process_stream(first_batch)

if __name__ == "__main__":
    main()
