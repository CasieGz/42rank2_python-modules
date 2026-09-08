#!/usr/bin/env python3

if __name__ == "__main__":
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print("Plant: " + name)
    print(f"Height: {height}cm")
    if age > 1:
        print(f"Age: {age} days")
    else:
        print(f"Age: {age} day")
    print("\n=== End of Program ===")
