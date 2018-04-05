from Decision_Tree import *
from decimal import *
from random import shuffle



def kFoldCrossValidation(dataSet, attributes, targetAttribute, method, k):
    accuracyAverage = 0
    results = []

    for i in range(k):
        score = 0.0
        trainSet = dataSet[:]
        testSet = makeTestSet(dataSet, trainSet, k)

        tree = DECISION_TREE_LEARNING(trainSet, attributes, targetAttribute, None, method)

        for record in testSet:
            if classification(tree, record) is not 'Null':
                score = score + 1.0

        accuracy = (score / len(testSet))*100
        accuracyAverage = accuracyAverage + accuracy
        results.append(float(Decimal(accuracy).quantize(Decimal('0.01'))))
        print "Test", i+1, "/", k, " of method ", method, ", complete!"
    print
    return results, Decimal(accuracyAverage/k).quantize(Decimal('0.01'))


def makeTestSet(dataSet, trainSet, k):
    testSet = []

    for j in range(0, len(dataSet) / k):
        shuffle(trainSet)
        testSet.append(trainSet.pop(0))
    return testSet


def classification(tree, record):
    if type(tree) == type("string"):
        return tree
    else:
        attribute = tree.keys()[0]
        if record[attribute] not in tree[attribute].keys():
            return 'Null'
        else:
            t = tree[attribute][record[attribute]]

        return classification(t, record)