import csv
import pathlib
import random

distribution_routes = dict()
bars = dict()
centers = dict()

deliveries = list()

DURATION = 50

results = list()

with open("Data/Centers.csv") as _f:
    r = csv.DictReader(_f)
    for row in r:
        name = row["CenterName"]
        del row["CenterName"]
        centers[name] = row
        centers[name]["NextApprovisioning"] = float(row["Approvisionment"])
        centers[name]["Volume"] = float(row["Capacity"])
        centers[name]["Approvisionment"] = float(row["Approvisionment"])
        centers[name]["Capacity"] = float(row["Capacity"])

with open("Data/Routes.csv") as _f:
    r = csv.DictReader(_f)
    for row in r:
        source = row["Source"]
        target = row["Target"]
        delay = row["Delay"]
        distribution_routes[(source, target)] = float(delay)

with open("Data/Bars.csv") as _f:
    r = csv.DictReader(_f)
    for row in r:
        name = row["BarName"]
        del row["BarName"]
        bars[name] = row
        bars[name]["Volume"] = float(row["Volume"])
        bars[name]["Consumption"] = float(row["Consumption"])

for day in range(DURATION):
    for center_name, center in centers.items():
        if center["NextApprovisioning"] == 0:
            center["Volume"] = center["Capacity"]
            center["NextApprovisioning"] = center["Approvisionment"]
        else:
            center["NextApprovisioning"] -= 1

    remaining_deliveries = list()
    upcoming_delivered_volumes = dict()
    for delivery in deliveries:
        if delivery["Time"] == day:
            bars[delivery["Bar"]]["Volume"] += delivery["Volume"]
        else:
            upcoming_delivered_volumes.setdefault(delivery["Bar"], 0)
            upcoming_delivered_volumes[delivery["Bar"]] += delivery["Volume"]
            remaining_deliveries.append(delivery)
    deliveries = remaining_deliveries

    _bars = list(bars.items())
    random.shuffle(_bars)
    _centers = list(centers.items())
    random.shuffle(_centers)
    for bar_name, bar in _bars:
        best_delivery = 0
        best_delivery_duration = 0
        best_center = None
        for center_name, center in _centers:
            delivery_duration = distribution_routes.get((center_name, bar_name))
            volume = min(center["Volume"], (bar["Volume"] - bar["Consumption"] * delivery_duration))
            volume -= upcoming_delivered_volumes.get(bar_name, 0)
            if volume > best_delivery:
                best_delivery = volume
                best_center = center_name
                best_delivery_duration = delivery_duration
        if best_center is not None:
            deliveries.append(
                {"Bar": bar_name, "Time": day + best_delivery_duration, "Volume": best_delivery, "Center": best_center})
            centers[best_center]["Volume"] -= best_delivery
            results.append(
                {"Bar": bar_name, "Depart": day, "Volume": best_delivery, "Center": best_center})

pathlib.Path("Results").mkdir(parents=True, exist_ok=True)
with open("Results/Results.csv", "w") as _f:
    w = csv.DictWriter(_f, fieldnames=["Bar", "Depart", "Volume", "Center"])
    w.writeheader()
    for delivery in results:
        w.writerow(delivery)
        print(delivery)
