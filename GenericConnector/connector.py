import csv
import random

bars = list()
centers = ["One", "Two"]
routes = list()

with open("Client/Original/data.csv") as _f:
    r = csv.DictReader(_f)
    for row in r:
        row["Volume"] = 10
        bars.append(row)
        for center in centers:
            routes.append({
                "Source": center,
                "Target": row["BarName"],
                "Delay": random.randint(1, 10)
            })

with open("Data/Routes.csv", "w") as _f:
    w = csv.DictWriter(_f, fieldnames=["Source", "Target", "Delay"])
    w.writeheader()
    for route in routes:
        w.writerow(route)

with open("Data/Bars.csv", "w") as _f:
    w = csv.DictWriter(_f, fieldnames=["BarName", "Volume", "Consumption"])
    w.writeheader()
    for bar in bars:
        w.writerow(bar)
