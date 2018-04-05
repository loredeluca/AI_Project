import random
from random import shuffle


def readDataSet(filename, prob):
    file = open(filename, 'r')

    lines = [line.strip() for line in file.readlines()]
    attributes = [attribute.strip() for attribute in lines.pop(0).split(",")]
    targetAttribute = attributes[len(attributes)-1]

    dataSet = []
    for line in lines:
        dataSet.append(dict(zip(attributes, [element.strip() for element in line.split(",")])))
    file.close()

    shuffle(dataSet)
    newDataSet = depopulateDataSet(dataSet, attributes, targetAttribute, prob)

    return newDataSet, attributes, targetAttribute


def depopulateDataSet(dataSet, attributes, targetAttribute, prob):
    # Sceglie con probabilita' p un record del data set, e ne elimina un attributo
    for i in range(0, len(dataSet)-1):
        x = random.random()
        if x <= prob:
            d = dataSet[i]
            # Sceglie l'attributo da rimuovere
            y = random.randint(0, len(attributes)-1)
            if attributes[y] != targetAttribute:
                d[attributes[y]] = '?'

    return dataSet