#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class InvalidData(Exception):
    def __init__(self, message: str = "Invalid Data"):
        self.message = message


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.processing_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank_to_return = self.processing_rank
        self.processing_rank += 1
        oldest_data = self.storage.pop(0)
        return (rank_to_return, oldest_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and type(data) is not bool:
            return True
        if isinstance(data, list) and len(data) > 0 and all(
            # checking for not bool since bool True is equal to 1 so
            # if we input isinstance(True, int) this will return
            # true eventhough its false for us
                isinstance(x, (int, float)) and type(x) is not bool
                for x in data
                ):
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise InvalidData("Improper numeric data")

        if isinstance(data, list):
            # list comprehension: turning every object into
            # a string and giving the whole list[str] to extend
            self.storage.extend([str(num) for num in data])
        else:
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0 and all(
                isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise InvalidData("Improper string data")

        if isinstance(data, list):
            self.storage.extend(data)
        else:
            self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            # items() gets the key and value
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())

        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(entry, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in entry.items()
                )
                for entry in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise InvalidData("Improper dict data")

        if isinstance(data, list):
            for entry in data:
                str_construct = ": ".join(entry.values())
                self.storage.append(str_construct)
        else:
            str_construct = ": ".join(data.values())
            self.storage.append(str_construct)


# ex1 starting here
class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """register a new data processor to process the data stream"""
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """analyze each element of the list received as a parameter and send
        it to the appropriate registered data processor. Error messages will be
        printed if no data processor can handle an element"""
        for element in stream:
            for proc in self.processors:
                try:
                    if proc.validate(element):
                        proc.ingest(element)
                        break
                except InvalidData:
                    pass
            else:
                print("DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        """print stream statistics"""
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            raw_name = proc.__class__.__name__
            display_name = raw_name.replace("Processor", " Processor")
            total = len(proc.storage) + proc.processing_rank

            print(f"{display_name}: total {total} items processed, remaining "
                  f"{len(proc.storage)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    data_stream.register_processor(NumericProcessor())

    data_batch: Any = ['Hello world', [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                        'log_message': 'User wil is connected'}],
                       42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {data_batch}")
    data_stream.process_stream(data_batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(data_batch)
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for proc in data_stream.processors:
        if isinstance(proc, NumericProcessor):
            for _ in range(3):
                proc.output()
        elif isinstance(proc, TextProcessor):
            for _ in range(2):
                proc.output()
        elif isinstance(proc, LogProcessor):
            proc.output()

    data_stream.print_processors_stats()
