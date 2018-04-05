import random


def Method_A(data, attribute):
    # Suppongo che l'esempio abbia tutti i possibili valori dell'attributo,
    # pesando pero' ognuno di essi in base alla sua frequenza negli esempi
    # che raggiungono quel nodo.
    val_freq = {}
    count = 0

    # calcolo la frequenza di ciascun attributo che abbia un valore
    for record in data:
        if record[attribute] in val_freq:
            val_freq[record[attribute]] += 1.0
            count += 1
        elif record[attribute] not in val_freq and record[attribute] != '?':
            val_freq[record[attribute]] = 1.0
            count += 1

    prob_val = val_freq.copy()

    # calcolo la probabilita' di ciascun attributo
    for val in val_freq.keys():
        prob_val[val] = val_freq[val]/count

    probAtt = []
    valAtt = []

    for val in prob_val.keys():
        probAtt.append(prob_val[val])
        valAtt.append(val)

    for i in range(len(probAtt)):
        if i == 0:
            probAtt[i] = probAtt[i]
        else:
            probAtt[i] = probAtt[i]+probAtt[i-1]

    x = random.random()
    for p in probAtt:
        if x < p:
            scelta = p
            break

    for i in range(len(probAtt)):
        if probAtt[i] == scelta:
            l = i

    newValue = valAtt[l]

    return newValue


def Method_B(data, attribute):
    # Gli esempi a cui manca qualcuno degli attributi ricevono valori stimati
    # in base alla frequenza dei valori nel dataSet
    val_freq = {}
    equalVal_freq = []
    valMax = 0

    # calcolo la frequenza di ciascun attributo che abbia un valore
    for record in data:
        if record[attribute] in val_freq:
            val_freq[record[attribute]] += 1.0
        elif record[attribute] not in val_freq and record[attribute] != '?':
            val_freq[record[attribute]] = 1.0

    # calcolo il valore a frequenza massima
    for val in val_freq.keys():
        if val_freq[val] > valMax:
            valMax = val_freq[val]

    # gestisco il caso in cui piu' di un attributo ha la stessa frequenza
    for val in val_freq.keys():
        if val_freq[val] == valMax:
            equalVal_freq.append(val)

    if len(equalVal_freq) > 1:
        x = random.randint(0, len(equalVal_freq)-1)
        newValue = equalVal_freq[x]
    else:
        newValue = equalVal_freq[0]

    return newValue


def importNewValueinDataSet(data, attributes, attribute, newValue, method, record):
    if method == 'A':
        for rec in data:
            if rec == record:
                for j in range(0, len(attributes) - 1):
                    if rec[attribute] == '?':
                        rec[attribute] = newValue

    elif method == 'B':
        for i in range(0, len(data)-1):
            d = data[i]
            for j in range(0, len(attributes)-1):
                if d[attribute] == '?':
                    d[attribute] = newValue