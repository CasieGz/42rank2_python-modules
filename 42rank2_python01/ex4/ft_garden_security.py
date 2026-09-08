#!/usr/bin/env python3

class Plant:

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float
    ) -> None:
        self._name = name
        self._growth = growth
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        if self._age_days > 1:
            days = "days"
        else:
            days = "day"
        print(f"{self._name}: {self._height}cm, {self._age_days} {days} old")

    def grow(self) -> None:
        self._height += self._growth
        self._height = round(self._height, 1)

    def age(self) -> None:
        self._age_days += 1

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age_days = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25.0)
    height = rose.get_height()
    print("\nHeight updated: 25cm")
    rose.set_age(30)
    age = rose.get_age()
    print(f"Age updated: {age} days\n")

    rose.set_height(-2)
    rose.set_age(-8)

    print("\nCurrent state: ", end="")
    rose.show()
