import csv
import json
import math


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)


    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def check_minimum_distance(x, y):
    if x < y:
        return x
    else:
        return y


def calculate_distance(x, y, x_c, y_c):
    result = math.sqrt((float(x) - x_c) ** 2 + (float(y) - y_c) ** 2)
    return result


def determine_cluster(c1, c2):
    if c1 < c2:
        return 'A'
    else:
        return 'B'


def start_iteration(dataset, centroid):
    result = []

    centroid_A = centroid["A"]
    centroid_B = centroid["B"]

    for i in dataset:
        distance_A = calculate_distance(float(i["X"]), float(i["Y"]), centroid_A["X"], centroid_A["Y"])
        distance_B = calculate_distance(float(i["X"]), float(i["Y"]), centroid_B["X"], centroid_B["Y"])
        result.append({
            "ID": int(i["ID"]),
            "Distance_A": distance_A,
            "Distance_B": distance_B,
            "Minimum_Distance": check_minimum_distance(distance_A, distance_B),
            "Cluster": determine_cluster(distance_A, distance_B)
        })
    return result


csvFilePath = r'DATA.csv'
jsonFilePath = r'file.json'
csv_to_json(csvFilePath, jsonFilePath)

centroid = {
    "A": {
        "X": 6,
        "Y": 9
    },
    "B": {
        "X": 2,
        "Y": 8
    }
}

dataset = json.load(open('file.json'))
result = start_iteration(dataset, centroid)
print(result)
