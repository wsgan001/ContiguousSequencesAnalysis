from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


def accuracy_score_with_unclassified_objects(y, y_predict):
    y_new = []
    y_predict_new = []
    number_of_unclassified = 0

    for i in xrange(len(y)):
        if y_predict[i] != -1:
            y_new.append(y[i])
            y_predict_new.append(y_predict[i])
        else:
            number_of_unclassified += 1

    accuracy = accuracy_score(y_new, y_predict_new)

    return accuracy, number_of_unclassified


def tpr_fpr_nonclass(y, y_predict):
    y_new = []
    y_predict_new = []
    number_of_unclassified = 0

    for i in xrange(len(y)):
        if y_predict[i] != -1:
            y_new.append(y[i])
            y_predict_new.append(y_predict[i])
        else:
            number_of_unclassified += 1

    confusion_m = confusion_matrix(y_new, y_predict_new)
    print(confusion_m)
    if confusion_m != []:
        tp = confusion_m[1, 1]
        fp = confusion_m[0, 1]

        tn = confusion_m[0, 0]
        fn = confusion_m[1, 0]

        pos = tp + fn
        neg = tn + fp

        tpr = tp/float(pos)
        fpr = fp/float(neg)
    else:
        tpr = 0
        fpr = 0

    return tpr, fpr, number_of_unclassified


def f1_score_nonclass(y, y_predict):
    y_new = []
    y_predict_new = []
    number_of_unclassified = 0

    for i in xrange(len(y)):
        if y_predict[i] != -1:
            y_new.append(y[i])
            y_predict_new.append(y_predict[i])
        else:
            number_of_unclassified += 1

    f1 = f1_score(y_new, y_predict_new)

    return f1, number_of_unclassified