import csv
import random


class DataHandler:
    def __init__(self):
        pass

    @staticmethod
    def getData(trainingSet=[] , testSet=[]):
        with open("input.txt") as csvFile:
            lines = csv.reader(csvFile)
            dataset = list(lines)
            for x in range(len(dataset) - 1):
                for y in range(24):
                    dataset[x][y] = float(dataset[x][y])
                if random.random() < 0.8:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])

