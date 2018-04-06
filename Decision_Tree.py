import math
from Missing_Attribute import *


def DECISION_TREE_LEARNING(examples, attributes, targetAttribute, parent_examples, method):
    # mette in vals tutti i valori del targetAttribute
    vals = [record[targetAttribute] for record in examples]

    if not examples:
        return pluralityValue(parent_examples, targetAttribute)
    elif (len(attributes)-1) <= 0:
        return pluralityValue(examples, targetAttribute)
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        A = importance(attributes, examples, targetAttribute, method)
        tree = {A: {}}
        # bestAttribute_value contiene tutti i valori che il bestAttribute puo' assumere
        bestAttribute_value = get_values(examples, A)

        # costruisco il sottoalbero con chiamata ricorsiva dopo aver definito subExamples e subAttributes
        for value in bestAttribute_value:
            subExamples = build_subExamples(examples, A, value)
            subAttributes = [att for att in attributes if att != A]
            subTree = DECISION_TREE_LEARNING(subExamples, subAttributes, targetAttribute, examples, method)

            tree[A][value] = subTree

    return tree


def get_values(dataSet, bestAtt):
    value = []

    for record in dataSet:
        value.append(record[bestAtt])
    value = set(value)
    return value


def build_subExamples(dataSet, attribute, val):
    # La funzione costruisce il subDataSet,
    # ogni record che ha come attribute il valore val, viene inserito nel subDataSet
    subDataset = []

    for record in dataSet:
        if record[attribute] == val:
            subDataset.append(record)

    return subDataset


def pluralityValue(dataSet, targetAttribute):
    # La funzione ritorna il valore ripetuto piu' volte di targetAttribute
    vals = [record[targetAttribute] for record in dataSet]
    maxFreq = 0
    mostFreq = None

    value = []

    for record in dataSet:
        value.append(record[targetAttribute])
    value = set(value)

    for i in value:
        if vals.count(i) > maxFreq:
            maxFreq = vals.count(i)
            mostFreq = i

    return mostFreq


def importance(attributes, dataSet, targetAttribute, method):
    # La funzione determina l'attributo con information gain maggiore

    bestGain = 0
    bestAttribute = None

    for att in attributes:
        g = gain(dataSet, attributes, att, targetAttribute, method)

        if g >= bestGain and att != targetAttribute:
            bestGain = g
            bestAttribute = att

    return bestAttribute


def gain(dataSet, attributes, attribute, targetAttribute, method):
        val_freq = {}
        vectorNull = []
        for i in range(len(attributes)):
            vectorNull.append('NULL')
        # creo un dizionario in cui ciascun attributo ha valore 'NULL'
        newValues = dict(zip(attributes, vectorNull))

        if method == 'A':
            # calcola la frequenza di ogni attributo all'interno del dataSet
            for record in dataSet:
                if record[attribute] in val_freq:
                    val_freq[record[attribute]] += 1.0
                elif record[attribute] == '?':
                    newValues[attribute] = Method_A(dataSet, attribute)
                    importNewValueinDataSet(dataSet, attributes, attribute, newValues[attribute], method, record)
                    if newValues[attribute] in val_freq:
                        val_freq[newValues[attribute]] += 1.0
                    else:
                        val_freq[newValues[attribute]] = 1.0
                else:
                    val_freq[record[attribute]] = 1.0

        elif method == 'B':
            for record in dataSet:
                if record[attribute] in val_freq:
                    val_freq[record[attribute]] += 1.0
                elif record[attribute] == '?':
                    # controllo che il newValues non sia gia stato calcolato
                    if newValues[attribute] == 'NULL':
                        newValues[attribute] = Method_B(dataSet, attribute)
                    importNewValueinDataSet(dataSet, attributes, attribute, newValues[attribute], method, record)
                    if newValues[attribute] in val_freq:
                        val_freq[newValues[attribute]] += 1.0
                    else:
                        val_freq[newValues[attribute]] = 1.0
                else:
                    val_freq[record[attribute]] = 1.0

        subsetEntropy = 0.0

        for val in val_freq.keys():
            val_prob = val_freq[val] / sum(val_freq.values())
            data_subset = [record for record in dataSet if record[attribute] == val]
            subsetEntropy = subsetEntropy + val_prob * entropy(data_subset, targetAttribute)

        return entropy(dataSet, targetAttribute) - subsetEntropy


def entropy(data, Targetattribute):
        val_freq = {}
        entropy = 0.0

        for record in data:
            if record[Targetattribute] in val_freq:
                val_freq[record[Targetattribute]] += 1.0
            else:
                val_freq[record[Targetattribute]] = 1.0

        for freq in val_freq.values():
            entropy = entropy + (-freq / len(data)) * math.log(freq / len(data), 2)

        return entropy