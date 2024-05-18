from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import os


# Building confusion matrix
def evaluate_classification(model, name, train_list, subfolder, setType):
    # Setting lists
    X_train = train_list[0]
    X_test = train_list[1]
    y_train = train_list[2]
    y_test = train_list[3]

    # Metric calculation
    train_accuracy = metrics.accuracy_score(y_train, model.predict(X_train))
    test_accuracy = metrics.accuracy_score(y_test, model.predict(X_test))

    train_precision = metrics.precision_score(y_train, model.predict(X_train))
    test_precision = metrics.precision_score(y_test, model.predict(X_test))

    train_recall = metrics.recall_score(y_train, model.predict(X_train))
    test_recall = metrics.recall_score(y_test, model.predict(X_test))

    train_loss = metrics.mean_squared_error(y_train, model.predict(X_train))
    test_loss = metrics.mean_squared_error(y_test, model.predict(X_test))

    # CLI Printing
    kernel_evals = dict()
    kernel_evals[str(name)] = [train_accuracy, test_accuracy, train_precision, test_precision, train_recall,
                               test_recall, train_loss, test_loss]
    print("Training Accuracy " + str(name) + " {}  Test Accuracy ".format(train_accuracy * 100) + str(
        name) + " {}".format(
        test_accuracy * 100))
    print(
        "Training Precision " + str(name) + " {}  Test Precision ".format(train_precision * 100) + str(
            name) + " {}".format(
            test_precision * 100))
    print("Training Recall " + str(name) + " {}  Test Recall ".format(train_recall * 100) + str(name) + " {}".format(
        test_recall * 100))
    print("Training Loss " + str(name) + " {}  Test Loss ".format(train_loss * 100) + str(name) + " {}".format(
        test_loss * 100))

    # Confusion Matrix
    actual = y_test
    predicted = model.predict(X_test)
    confusion_matrix = metrics.confusion_matrix(actual, predicted)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=['normal', 'attack'])

    # Showing and Export
    filename = subfolder + "\\" + name + "_CM.png"
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.grid(False)
    cm_display.plot(ax=ax)

    plt.title("Confusion Matrix for " + name + " Against " + setType + " Dataset")
    plt.savefig(filename)
    plt.show()
    return [test_accuracy, test_precision, test_recall, test_loss]


def alg_test(classifier, classifierName, train_list, subfolder, setType):
    classifier.fit(train_list[0], train_list[2])  # I0 = x train; I2 = y train
    classifierResults = evaluate_classification(classifier, classifierName, train_list, subfolder, setType)
    return classifierResults


# Displaying results in more graphs
def barGraph(valueDict, metric, setType, subfolder):
    barX = list(valueDict.keys())
    barY = list(valueDict.values())

    filename = subfolder + "\\ML" + metric + ".png"
    plt.figure(figsize=(15, 7))

    plt.bar(barX, barY, width=0.4)
    plt.xlabel("Classifying Algorithms")
    plt.ylabel("Percentage (%)")
    plt.title(metric + " of Classifiers Against " + setType + " Dataset")
    plt.savefig(filename)
    # plt.show()


def trainSet(train_choice, setType, resultFolder):
    print("Using a " + setType + " dataset")

    #Create sub-folder
    subfolder = resultFolder + "\\" + setType
    os.makedirs(subfolder)

    # Testing various algorithms
    lin_svc = LinearSVC()
    lin_svc_results = alg_test(lin_svc, "LinearSVC", train_choice, subfolder, setType)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn_results = alg_test(knn, "KNeighborsClassifier", train_choice, subfolder, setType)

    rf = RandomForestClassifier()
    rf_results = alg_test(rf, "RandomForestClassifier", train_choice, subfolder, setType)

    mlp = MLPClassifier(hidden_layer_sizes=(20, 5))
    mlp_results = alg_test(mlp, "MLPClassifier", train_choice, subfolder, setType)

    MLAcc = {
        "Support Vector Machines": lin_svc_results[0] * 100,
        "K-Nearest Neighbor": knn_results[0] * 100,
        "Random Forest": rf_results[0] * 100,
        "Multi Layer Perceptron": mlp_results[0] * 100
    }

    barGraph(MLAcc, "Accuracy", setType, subfolder)

    MLPre = {
        "Support Vector Machines": lin_svc_results[1] * 100,
        "K-Nearest Neighbor": knn_results[1] * 100,
        "Random Forest": rf_results[1] * 100,
        "Multi Layer Perceptron": mlp_results[1] * 100
    }

    barGraph(MLPre, "Precision", setType, subfolder)

    MLRe = {
        "Support Vector Machines": lin_svc_results[2] * 100,
        "K-Nearest Neighbor": knn_results[2] * 100,
        "Random Forest": rf_results[2] * 100,
        "Multi Layer Perceptron": mlp_results[2] * 100
    }

    barGraph(MLRe, "Recall", setType, subfolder)

    MLLoss = {
        "Support Vector Machines": lin_svc_results[3] * 100,
        "K-Nearest Neighbor": knn_results[3] * 100,
        "Random Forest": rf_results[3] * 100,
        "Multi Layer Perceptron": mlp_results[3] * 100
    }

    barGraph(MLLoss, "Loss", setType, subfolder)

    alg_results = [lin_svc_results, knn_results, rf_results, mlp_results]
    AR_columns = ["Accuracy", "Precision", "Recall", "Loss"]
    AR_labels = ["Support Vector Machines", "K-Nearest Neighbor", "Random Forest", "Multi Layer Perceptron"]
    alg_results_df = pd.DataFrame(alg_results, index=AR_labels, columns=AR_columns)

    print(alg_results_df)
    return alg_results_df
