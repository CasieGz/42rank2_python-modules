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


# The isinstance() function returns True if the specified object is
# of the specified type, otherwise False.
# The all() function returns True if all items in an iterable are true,
# otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # Testing Numeric Processor
    print("\nTesting Numeric Processor...")
    num_processor = NumericProcessor()
    test_num = 42
    print(f"Trying to validate input '{test_num}': "
          f"{num_processor.validate(test_num)}")

    test_str = "Hello"
    print(f"Trying to validate input '{test_str}': "
          f"{num_processor.validate(test_str)}")

    test_str = "foo"
    try:
        print(f"Test invalid ingestion of string "
              f"'{test_str}' without prior validation:")
        num_processor.ingest(test_str)  # type: ignore
    except InvalidData as e:
        print(f"Got exception: {e}")

    test_list1: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_list1}")
    if num_processor.validate(test_list1):
        num_processor.ingest(test_list1)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num_processor.output()
        print(f"Numeric value {rank}: {value}")

    # Testing Text Processor
    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    test_num = 42
    print(f"Trying to validate input '{test_num}': "
          f"{text_processor.validate(test_num)}")

    test_str = "Hello"
    print(f"Trying to validate input '{test_str}': "
          f"{text_processor.validate(test_str)}")

    test_num = 42
    try:
        print(f"Test invalid ingestion of number "
              f"'{test_num}' without prior validation:")
        text_processor.ingest(test_num)  # type: ignore
    except InvalidData as e:
        print(f"Got exception: {e}")

    test_list2: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {test_list2}")
    if text_processor.validate(test_list2):
        text_processor.ingest(test_list2)
    print("Extracting 1 value...")
    rank, value = text_processor.output()
    print(f"Text value {rank}: {value}")

    # Testing Log Processor
    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    test_num = 42
    print(f"Trying to validate input '{test_num}': "
          f"{log_processor.validate(test_num)}")

    test_str = "Hello"
    print(f"Trying to validate input '{test_str}': "
          f"{log_processor.validate(test_str)}")

    test_str = "foo"
    try:
        print(f"Test invalid ingestion of string "
              f"'{test_str}' without prior validation:")
        log_processor.ingest(test_str)  # type: ignore
    except InvalidData as e:
        print(f"Got exception: {e}")

    test_list3: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {test_list3}")
    if log_processor.validate(test_list3):
        log_processor.ingest(test_list3)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log_processor.output()
        print(f"Log entry {rank}: {value}")
