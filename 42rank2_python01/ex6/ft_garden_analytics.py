#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count}"
                  f" age, {self._show_count} show")

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
        self._stats = Plant.Stats()

    def show(self) -> None:
        self._stats.record_show()
        if self._age_days != 1:
            days = "days"
        else:
            days = "day"
        print(f"{self._name}: {self._height}cm, {self._age_days} {days} old")

    def grow(self, days: int = 1) -> None:
        self._stats.record_grow()
        for _ in range(days):  # underscore means the variable (i) is not used
            # and needed, so ignore, otherwise its error in unaccesed variable
            self._height += self._growth
            self._height = round(self._height, 1)

    def age(self, days: int = 1) -> None:
        self._stats.record_age()
        for _ in range(days):
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

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    @staticmethod
    def is_over_one_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float,
        color: str
    ) -> None:
        super().__init__(name, height, age_days, growth, color)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

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
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        self._stats.record_shade()
        self._shade_long = self._height
        self._shade_wide = self._trunk_diameter
        print(f"Tree {self._name} now produces a shade of {self._shade_long}cm"
              f" long and {self._shade_wide}cm wide.")

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

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self._nutritional_value += 1


def display_plant_stats(plant: Plant) -> None:
    name = plant.get_name()
    stats = plant.get_stats()
    print(f"[statistics for {name}]")
    stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_over_one_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_over_one_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.3, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)
