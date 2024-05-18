# Code Creator: Olaoluwa Adewoye
# Professor: Haydar Teymourlouei
# Department: Computer Technology
# University: Bowie State University
# Location: Bowie, Maryland, USA
# Date: May 2023

from AlgTest import trainSet
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import os
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from openpyxl import Workbook
from openpyxl.utils import dataframe

pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')


def setupFile(data_train):
    pd.set_option('display.max_columns', None)
    warnings.filterwarnings('ignore')

    columns = (
        ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
         'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
         'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
         'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
         'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
         'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
         'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'outcome', 'level'])

    data_train.columns = columns

    # Binary Classification
    data_train.loc[data_train['outcome'] == "normal", "outcome"] = 'normal'
    data_train.loc[data_train['outcome'] != 'normal', "outcome"] = 'attack'

    return data_train


def pie_plot(df, cols_list, rows, cols):
    fig, axes = plt.subplots(rows, cols)
    for ax, col in zip(axes.ravel(), cols_list):
        df[col].value_counts().plot(ax=ax, kind='pie', figsize=(15, 7), fontsize=10, autopct='%1.0f%%')
        ax.set_title(str(col), fontsize=12)
    plt.show()


def Scaling(df_num, cols):
    std_scaler = RobustScaler()
    std_scaler_temp = std_scaler.fit_transform(df_num)
    std_df = pd.DataFrame(std_scaler_temp, columns=cols)
    return std_df


def preprocess(dataframe):
    cat_cols = ['is_host_login', 'protocol_type', 'service', 'flag', 'land', 'logged_in', 'is_guest_login', 'level',
                'outcome']
    df_num = dataframe.drop(cat_cols, axis=1)
    num_cols = df_num.columns
    scaled_df = Scaling(df_num, num_cols)

    dataframe.drop(labels=num_cols, axis="columns", inplace=True)
    dataframe[num_cols] = scaled_df[num_cols]

    dataframe.loc[dataframe['outcome'] == "normal", "outcome"] = 0
    dataframe.loc[dataframe['outcome'] != 0, "outcome"] = 1

    dataframe = pd.get_dummies(dataframe, columns=['protocol_type', 'service', 'flag'])
    return dataframe


def createTrainTest(scaled_train):
    # Split dataset
    x = scaled_train.drop(['outcome', 'level'], axis=1).values
    y = scaled_train['outcome'].values
    y_reg = scaled_train['level'].values

    # Conduct PCA on inputs
    pca = PCA(n_components=20)
    pca = pca.fit(x)
    x_reduced = pca.transform(x)
    print("Number of original features is {} and of reduced features is {}".format(x.shape[1], x_reduced.shape[1]))

    # Format y
    y = y.astype('int')

    # Create splits
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    x_train_reduced, x_test_reduced, y_train_reduced, y_test_reduced = train_test_split(x_reduced, y, test_size=0.2,
                                                                                        random_state=42)
    x_train_reg, x_test_reg, y_train_reg, y_test_reg = train_test_split(x, y_reg, test_size=0.2, random_state=42)

    # Creating lists of everything to try
    train_normal = [x_train, x_test, y_train, y_test]
    train_PCA = [x_train_reduced, x_test_reduced, y_train_reduced, y_test_reduced]
    train_REG = [x_train_reg, x_test_reg, y_train_reg, y_test_reg]

    return [train_normal, train_PCA, train_REG]


def exportResults(*resultDFs, filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Classification Results"

    for resultdf in resultDFs:
        resultdf_rows = dataframe.dataframe_to_rows(resultdf, index=True, header=True)
        for row in resultdf_rows:
            ws.append(row)

    wb.save(filename)


def main():
    # Data Import and Labeling
    KDD_Data = pd.read_csv("KDDTest+.txt")
    KDD_Data = setupFile(KDD_Data)

    print(KDD_Data.head())

    # Display basic graphics
    pie_plot(KDD_Data, ['protocol_type', 'outcome'], 1, 2)

    # Scale data for better performance
    KDD_Data_scaled = preprocess(KDD_Data)

    # Create training/testing sets
    KDD_trainingSets = createTrainTest(KDD_Data_scaled)
    KDD_TT_Normal = KDD_trainingSets[0]
    KDD_TT_PCA = KDD_trainingSets[1]
    # KDD_TT_REG = KDD_trainingSets[2]

    # Create folder for storing data
    dupLabel = 1
    rootResultFolder = r'Results'
    if not os.path.exists(rootResultFolder):
        os.makedirs(rootResultFolder)

    folderName = r'Results\Results'
    while os.path.exists(folderName + str(dupLabel)):
        dupLabel += 1

    trueFolderName = folderName + str(dupLabel)
    os.makedirs(trueFolderName)

    # Test each set
    Normal_Results = trainSet(KDD_TT_Normal, "Normal", trueFolderName)
    PCA_Results = trainSet(KDD_TT_PCA, "PCA", trueFolderName)
    # Regressed_Results = trainSet(KDD_TT_REG, "Regressed") # Cannot be done as regressed factors are multiclass

    # Export to excel file
    excelName = trueFolderName + "\\" + "results.xlsx"
    exportResults(Normal_Results, PCA_Results, filename=excelName)


if __name__ == "__main__":
    main()
