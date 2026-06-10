def print_days(day: int, harvest: int):
    if day <= harvest:
        print(f"Day {day}")
        print_days(day + 1, harvest)


def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))
    print_days(1, harvest)
    print("Harvest time!")
