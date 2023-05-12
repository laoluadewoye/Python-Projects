import pandas as pd
import warnings
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

# Data Import and Labeling
data_train = pd.read_csv("KDDTest+.txt")

columns = (
    ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
     'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
     'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
     'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
     'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
     'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
     'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'outcome', 'level'])

data_train.columns = columns

print(data_train.head())

# Binary Classification
data_train.loc[data_train['outcome'] == "normal", "outcome"] = 'normal'
data_train.loc[data_train['outcome'] != 'normal', "outcome"] = 'attack'

print(data_train.head())

print(data_train.shape)


# Showcasing basic info about data
def pie_plot(df, cols_list, rows, cols):
    fig, axes = plt.subplots(rows, cols)
    for ax, col in zip(axes.ravel(), cols_list):
        df[col].value_counts().plot(ax=ax, kind='pie', figsize=(15, 7), fontsize=10, autopct='%1.0f%%')
        ax.set_title(str(col), fontsize=12)
    plt.show()


pie_plot(data_train, ['protocol_type', 'outcome'], 1, 2)


# Preprocessing Data
def Scaling(df_num, cols):
    std_scaler = RobustScaler()
    std_scaler_temp = std_scaler.fit_transform(df_num)
    std_df = pd.DataFrame(std_scaler_temp, columns=cols)
    return std_df


cat_cols = ['is_host_login', 'protocol_type', 'service', 'flag', 'land', 'logged_in', 'is_guest_login', 'level',
            'outcome']


def preprocess(dataframe):
    df_num = dataframe.drop(cat_cols, axis=1)
    num_cols = df_num.columns
    scaled_df = Scaling(df_num, num_cols)

    dataframe.drop(labels=num_cols, axis="columns", inplace=True)
    dataframe[num_cols] = scaled_df[num_cols]

    dataframe.loc[dataframe['outcome'] == "normal", "outcome"] = 0
    dataframe.loc[dataframe['outcome'] != 0, "outcome"] = 1

    dataframe = pd.get_dummies(dataframe, columns=['protocol_type', 'service', 'flag'])
    return dataframe


scaled_train = preprocess(data_train)

# Feature Reduction and Split
x = scaled_train.drop(['outcome', 'level'], axis=1).values
y = scaled_train['outcome'].values
y_reg = scaled_train['level'].values

pca = PCA(n_components=20)
pca = pca.fit(x)
x_reduced = pca.transform(x)
print("Number of original features is {} and of reduced features is {}".format(x.shape[1], x_reduced.shape[1]))

y = y.astype('int')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train_reduced, x_test_reduced, y_train_reduced, y_test_reduced = train_test_split(x_reduced, y, test_size=0.2,
                                                                                    random_state=42)
x_train_reg, x_test_reg, y_train_reg, y_test_reg = train_test_split(x, y_reg, test_size=0.2, random_state=42)

kernal_evals = dict()

# Creating lists of everything to try
train_normal = [x_train, x_test, y_train, y_test]
train_PCA = [x_train_reduced, x_test_reduced, y_train_reduced, y_test_reduced]
train_REG = [x_train_reg, x_test_reg, y_train_reg, y_test_reg]


# Building confusion matrix
def evaluate_classification(model, name, train_list):
    X_train = train_list[0]
    X_test = train_list[1]
    y_train = train_list[2]
    y_test = train_list[3]

    train_accuracy = metrics.accuracy_score(y_train, model.predict(X_train))
    test_accuracy = metrics.accuracy_score(y_test, model.predict(X_test))

    train_precision = metrics.precision_score(y_train, model.predict(X_train))
    test_precision = metrics.precision_score(y_test, model.predict(X_test))

    train_recall = metrics.recall_score(y_train, model.predict(X_train))
    test_recall = metrics.recall_score(y_test, model.predict(X_test))

    train_loss = metrics.mean_squared_error(y_train, model.predict(X_train))
    test_loss = metrics.mean_squared_error(y_test, model.predict(X_test))

    kernal_evals[str(name)] = [train_accuracy, test_accuracy, train_precision, test_precision, train_recall,
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

    actual = y_test
    predicted = model.predict(X_test)
    confusion_matrix = metrics.confusion_matrix(actual, predicted)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=['normal', 'attack'])

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.grid(False)
    cm_display.plot(ax=ax)
    plt.show()
    return [test_accuracy, test_precision, test_recall, test_loss]


def alg_test(classifier, classifierName, train_list):
    classifier.fit(train_list[0], train_list[2])  # I0 = x train; I2 = y train
    classifierResults = evaluate_classification(classifier, classifierName, train_list)
    return classifierResults


# You can choose train_normal, train_PCA, or train_REG
train_choice = train_PCA

# Testing various algorithms
lin_svc = svm.LinearSVC()
lin_svc_results = alg_test(lin_svc, "Linear SVC(LBasedImpl)", train_choice)

knn = KNeighborsClassifier(n_neighbors=20)
knn_results = alg_test(knn, "KNeighborsClassifier", train_choice)

rf = RandomForestClassifier()
rf_results = alg_test(rf, "RandomForestClassifier", train_choice)


# Displaying results in more graphs
def barGraph(valueDict, metric):
    barX = list(valueDict.keys())
    barY = list(valueDict.values())

    plt.figure(figsize=(15, 7))

    plt.bar(barX, barY, width=0.4)
    plt.xlabel("Classifying Algorithms")
    plt.ylabel("Percentage (%)")
    plt.title(metric + " of Classifiers")
    plt.show()


MLAcc = {
    "Support Vector Machines": lin_svc_results[0] * 100,
    "K-Nearest Neighbor": knn_results[0] * 100,
    "Random Forest": rf_results[0] * 100
}

barGraph(MLAcc, "Accuracy")

MLPre = {
    "Support Vector Machines": lin_svc_results[1] * 100,
    "K-Nearest Neighbor": knn_results[1] * 100,
    "Random Forest": rf_results[1] * 100
}

barGraph(MLAcc, "Precision")

MLRe = {
    "Support Vector Machines": lin_svc_results[2] * 100,
    "K-Nearest Neighbor": knn_results[2] * 100,
    "Random Forest": rf_results[2] * 100
}

barGraph(MLAcc, "Recall")

MLLoss = {
    "Support Vector Machines": lin_svc_results[3] * 100,
    "K-Nearest Neighbor": knn_results[3] * 100,
    "Random Forest": rf_results[3] * 100
}

barGraph(MLLoss, "Loss")
