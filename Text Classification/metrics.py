import numpy as np

def calculate_metrics(y_true, y_pred, number_of_classes):
    # Confusion Matrix
    cm = np.zeros((number_of_classes, number_of_classes), dtype=int)

    for i in range(len(y_true)):
        actual_class = y_true[i]
        predicted_class = y_pred[i]

        cm[actual_class, predicted_class] += 1

    # Rest of the metrics
    precision_list = []
    recall_list = []
    f1_list = []

    # Use CM to get the rest of the metrics
    for class_label in range(number_of_classes):

        # FN is when the actual class is current class but predicted incorrectly
        # FP is when the predicted class is current class but actual is different

        TP = cm[class_label, class_label]
        FN = np.sum(cm[class_label, :]) - TP # Sum the class row - TP
        FP = np.sum(cm[:, class_label]) - TP # Sum the class column - TP

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        precision_list.append(precision)
        recall_list.append(recall)
        f1_list.append(f1_score)

    # Get macro averaged metrics
    macro_precision = np.mean(precision_list)
    macro_recall = np.mean(recall_list)
    macro_f1 = np.mean(f1_list)

    return cm, macro_precision, macro_recall, macro_f1