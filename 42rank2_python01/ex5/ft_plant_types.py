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


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float,
        color: str
    ) -> None:
        super().__init__(name, height, age_days, growth)
        self._color = color
        self._bloom_status: bool = False

    def bloom(self) -> None:
        self._bloom_status = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._bloom_status:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days, growth)
        self._trunk_diameter = trunk_diameter
        self._shade_long = 0.0
        self._shade_wide = 0.0

    def produce_shade(self) -> None:
        self._shade_long = 200.0
        self._shade_wide = 5.0
        print(f"Tree {self._name} now produces a shade of {self._shade_long}"
              f"cm long and {self._shade_wide}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age_days, growth)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.3, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April",)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
