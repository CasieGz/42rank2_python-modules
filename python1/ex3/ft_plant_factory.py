#!/usr/bin/env python3

class Plant:

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = growth

    def show(self) -> None:
        if self.age_days > 1:
            days = "days"
        else:
            days = "day"
        print(f"{self.name}: {self.height}cm, {self.age_days} {days} old")

    def grow(self) -> None:
        self.height += self.growth
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    oak = Plant("Oak", 200.0, 365, 0.5)
    cactus = Plant("Cactus", 5.0, 90, 0.1)
    sunflower = Plant("Sunflower", 80.0, 45, 1.6)
    fern = Plant("Fern", 15.0, 120, 2.1)
    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
