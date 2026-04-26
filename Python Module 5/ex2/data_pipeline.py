from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
        self.total_processed = 0
    """
    We delete de oldest element in the list with pop(0)
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
            self.total_processed += len(data)
            return
        self.data.append(str(data))
        self.total_processed += 1


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
            self.total_processed += len(data)
            return
        self.data.append(data)
        self.total_processed += 1


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
            self.total_processed += 1
            return
        elif isinstance(data, list):
            for item in data:
                log_entry = f"{item['log_level']}: {item['log_message']}"
                self.data.append(log_entry)
            self.total_processed += len(data)
            return


class CSVPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = ""
        i = 0
        for element in data:
            if i == 0:
                result += element[1]
                i += 1
            else:
                string = "," + element[1]
                result += string
        print("CSV Output:")
        print(result)


class JSONPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = {}
        for element in data:
            item = f"item_{element[0]}"
            result[item] = str(element[1])
        print(result)


class DataStream:
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
                    break
            if not processed:
                print(f"DataStream error -"
                      f" Can't process element in stream: {element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processor_list:
            data: list[tuple[int, str]] = []
            for x in range(nb):
                if processor.data:
                    item = processor.output()
                    data.append(item)
                else:
                    break
            plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if self.processor_list == []:
            print("No processor found, no data")
            return
        for processor in self.processor_list:
            name = processor.__class__.__name__.replace(
                "Processor", " Processor")
            print(f"{name}: total {processor.total_processed} items processed,"
                  f" remaining {len(processor.data)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    data_stream = DataStream()
    print()
    data_stream.print_processors_stats()
    print()
    print("Registering Processors")
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    first_batch = ['Hello world', [3.14, -1, 2.71],
                   [{'log_level': 'WARNING',
                     'log_message': 'Telnet access! Use ssh instead'},
                    {'log_level': 'INFO',
                    'log_message': 'User wil isconnected'}],
                   42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {first_batch}")
    print()
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    print()
    data_stream.print_processors_stats()
    print()
    second_batch = [21, ['I love AI',
                         'LLMs are wonderful', 'Stay healthy'],
                        [{'log_level': 'ERROR',
                          'log_message': '500 server crash'},
                         {'log_level': 'NOTICE',
                          'log_message': 'Certificateexpires in 10 days'}],
                        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data on stream: {second_batch}")
    data_stream.process_stream(second_batch)
    print()
    data_stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin")
    json_plugin = JSONPlugin()
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
