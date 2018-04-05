from CrossValidation import kFoldCrossValidation
from DataSet import *

dataSets = ["cardata.csv", "tris.csv", "mushrooms.csv"]
p = [0, 0.05, 0.1, 0.2, 0.3]

def test(DataSet, prob, k):
    data, attributes, targetAttribute = readDataSet(DataSet, prob)

    scores = []
    accuracyAverage = []

    methodA = kFoldCrossValidation(data, attributes, targetAttribute, 'A', k)
    methodB = kFoldCrossValidation(data, attributes, targetAttribute, 'B', k)

    scores.append(methodA[0])
    scores.append(methodB[0])

    accuracyAverage.append(methodA[1])
    accuracyAverage.append(methodB[1])

    return scores, accuracyAverage

def main(k):
    for i in range(0, len(dataSets)):
        for j in range(0, len(p)):
            print k, "-Fold Cross Validation: "
            print "DataSet " + dataSets[i] + ' with probability : ' + str(p[j])
            results = test(dataSets[i], p[j], k)
            print
            print "Scores for MethodA : " + str(results[0][0]) + "  -->  Average : " + str(results[1][0])
            print "Scores for MethodB: " + str(results[0][1]) + "  -->  Average : " + str(results[1][1])
            print

main(5)
