#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age_days: int
    growth: float

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
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    rose.growth = 0.8
    rose.show()

    start_height: float = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth_week: float = round(rose.height - start_height, 1)
    print(f"Growth this week: {growth_week}cm")
