#!/usr/bin/env python3

from importlib import metadata
import sys

PACKAGE_INFO = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    all_dependencys_installed: bool = True
    for dependency in PACKAGE_INFO:
        try:
            feedback = (f"[OK] {dependency} "
                        f"({metadata.version(dependency)})"
                        f" - {PACKAGE_INFO[dependency]}")
            print(feedback)
        except metadata.PackageNotFoundError:
            print(f"[WARNING]: Missing dependency '{dependency}'")
            all_dependencys_installed = False
    return all_dependencys_installed


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    all_dependencys_installed = check_dependencies()

    if not all_dependencys_installed:
        print("\nTo install missing dependencys with pip do:")
        print("pip install -r requirements.txt")
        print("python3 loading.py\n")
        print("To install missing dependencys with poetry do:")
        print("poetry install")
        print("poetry run python loading.py\n")
        sys.exit(1)

    # this only runs if all dependencys are installed
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    crypto_url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=eur&order=market_cap_desc&per_page=5"
    )
    response = requests.get(crypto_url)
    if response.status_code == 200:
        data = response.json()
        # list comprehension: take every str from the key 'name'
        names = [coin['name'] for coin in data]
        # market cap is the value of f.ex. one bitcoin
        # times the amount of existing coins
        # we're deviding through 1 billion ergo 1 with 9 zeros
        market_cap = [coin['market_cap'] / 1e9 for coin in data]
        # the "{'market_cap':" is creating the column title
        crypto_analysis = pd.DataFrame({'market_cap': market_cap}, index=names)
        # bar diagram
        plt.bar(crypto_analysis.index, crypto_analysis['market_cap'])
        # givig it the x and y lable
        plt.title("Crypto Market Capitalization")
        plt.ylabel("Market Capitalization (Billion €)")
        plt.xlabel("Top 5 Cryptocurrencies")
        # saving it as a png
        plt.savefig("matrix_analysis.png")
    else:
        current_age = 25
        death = 89
        years_left = death - current_age
        # arrange() creates an array of evenly distributed
        # numbers within a specified interval.
        years = np.arange(current_age, death)
        # uniform generates a random float number in the specified range
        steps = np.random.uniform(-0.6, 0.6, size=years_left)
        start_screentime = 8.0
        # cumsum = cummulative sum: 8.0 + step1, then (8.0 + step1) + step2
        # creates then an np array
        screentime_raw = start_screentime + np.cumsum(steps)
        # we limit the values to stay realistic and round to 1 comma digit
        screentime = np.clip(screentime_raw, 1.0, 14.0).round(1)
        rotten_life = pd.DataFrame({
            'screentime_hours': screentime,
            'sleep_hours': (24 - screentime) * 0.5
            }, index=years)
        plt.plot(
            rotten_life.index, rotten_life['screentime_hours'],
            color='#FF1493', label='Screentime (h)'
            )
        plt.plot(
            rotten_life.index, rotten_life['sleep_hours'],
            color="#6614FF", label='Sleep (h)'
            )
        plt.legend()
        plt.xlabel("Age")
        plt.ylabel("Value")
        plt.title("Lifetime Habit Trend")
        plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
