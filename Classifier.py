# NOTE: To run this file, you need to type this command on the terminal: 'streamlit run Classifier.py'

import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, accuracy_score, precision_score, recall_score

st.title("Compare Different Classifiers")
st.subheader("Which one is best?")

classifier_name = st.sidebar.selectbox("Select Classifier", ("Naive Random Oversampler", "SMOTE Oversampler", "Undersampling", "SMOTEENN", "Random Forest Classifier", "AdaBoost Classifier"))


data = pd.read_csv('online_shoppers_intention.csv')
# url_name = 'https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/main/Resources/online_shoppers_intention.csv'
# data = pd.read_csv(url_name)

dataset_name = "online_shoppers_intention"

# Changed Revenue to dtype str
data['Revenue'] = data['Revenue'].astype('str')

# Replace True and False in Column Revenue by Sale or No Sale for better readability
data['Revenue'] = data['Revenue'].replace(['True'],'Sale')
data['Revenue'] = data['Revenue'].replace(['False'],'No Sale')


# Write dataset name to Streamlit
Sub_Title = "Dataset Name: " + dataset_name
st.subheader(Sub_Title)



# Split data into train and test
X = data.drop("Revenue", axis=1)
X = pd.get_dummies(X)

# Create our target variable
target=["Revenue"]
y = data.loc[:, target].copy()

# st.write("X: ", X)
# st.write("y: ", y)

# Make the train and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# X, y = get_dataset(dataset_name)
st.markdown("### Original Dataset")
st.write("Shape of Dataset", X.shape, "Number of classes", len(np.unique(y)))

# Model Selection
if classifier_name == "Naive Random Oversampler":
    st.subheader("Model: Naive Random Oversampler")
    
    # Resample the training data with the RandomOversampler
    from imblearn.over_sampling import RandomOverSampler
    strategy = st.sidebar.select_slider(
     'Select a sampling strategy',
     options=['auto', 'minority', 'not minority', 'not majority', 'all'])
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    ros = RandomOverSampler(sampling_strategy=strategy, random_state=Random_State_Seed)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
    st.write("Shape of Dataset", X_resampled.shape, "Number of classes", len(np.unique(y_resampled)))

    # Train the Logistic Regression model using the resampled data
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='lbfgs', random_state=1)
    model.fit(X_resampled, y_resampled)
    
    # Calculate predictions
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))
    
    # Print the classification report
    # from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_resampled.corr(), annot=False)
    st.pyplot(fig)
    
    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

elif classifier_name == "SMOTE Oversampler":
    st.subheader("Model: SMOTE Oversampler")

    # Resample the training data with the SMOTE oversampler
    from imblearn.over_sampling import SMOTE
    strategy = st.sidebar.select_slider(
        'Select a sampling strategy',
        options=['auto', 'minority', 'not minority', 'not majority', 'all'])
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    sm = SMOTE(sampling_strategy=strategy, random_state=Random_State_Seed)
    X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
    st.write("Shape of Dataset", X_resampled.shape, "Number of classes", len(np.unique(y_resampled)))

    # Train the Logistic Regression model using the resampled data
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='lbfgs', random_state=1)
    model.fit(X_resampled, y_resampled)

    # Calculate predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))
    
    # Print the classification report
    # from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot Feature Importance
    st.subheader("Feature Importance")
    fig = plt.figure(figsize=(10,10))
    sns.barplot(x=model.coef_[0], y=X_resampled.columns, orient='h')
    st.pyplot(fig)


    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_resampled.corr(), annot=False)
    st.pyplot(fig)

    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

elif classifier_name == "Undersampling":
    st.subheader("Model: Undersampling")

    # Resampling the data using the ClusterCentroids method
    from imblearn.under_sampling import ClusterCentroids
    strategy = st.sidebar.select_slider(
        'Select a sampling strategy',
        options=['auto', 'not minority', 'not majority', 'all'])
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    cc = ClusterCentroids(sampling_strategy=strategy, random_state=Random_State_Seed)
    X_resampled, y_resampled = cc.fit_resample(X_train, y_train)
    st.write("Shape of Dataset", X_resampled.shape, "Number of classes", len(np.unique(y_resampled)))

    # Train the Logistic Regression model using the resampled data
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='lbfgs', random_state=1)
    model.fit(X_resampled, y_resampled)

    # Calculate predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))

    # Print the classification report
    from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot Feature Importance
    st.subheader("Feature Importance")
    fig = plt.figure(figsize=(10,10))
    sns.barplot(x=model.coef_[0], y=X_resampled.columns, orient='h')
    st.pyplot(fig)
    
    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_resampled.corr(), annot=False)
    st.pyplot(fig)

    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

elif classifier_name == "SMOTEENN":
    st.write("Model: SMOTEENN")

    # Resampling the data using the SMOTEENN method
    from imblearn.combine import SMOTEENN
    strategy = st.sidebar.select_slider(
        'Select a sampling strategy',
        options=['minority', 'not minority', 'not majority', 'all', 'auto'])
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    sm = SMOTEENN(sampling_strategy=strategy, random_state=Random_State_Seed)
    X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
    st.write("Shape of Dataset", X_resampled.shape, "Number of classes", len(np.unique(y_resampled)))

    # Train the Logistic Regression model using the resampled data
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='lbfgs', random_state=1)
    model.fit(X_resampled, y_resampled)

    # Calculate predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))

    # Print the classification report
    from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot Feature Importance
    st.subheader("Feature Importance")
    fig = plt.figure(figsize=(10,10))
    sns.barplot(x=model.coef_[0], y=X_resampled.columns, orient='h')
    st.pyplot(fig)
    
    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_resampled.corr(), annot=False)
    st.pyplot(fig)

    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

elif classifier_name == "Random Forest Classifier":
    st.write("Model: Random Forest Classifier")

    # Train the Random Forest Classifier model using the training set
    from imblearn.ensemble import BalancedRandomForestClassifier
    features = st.sidebar.select_slider(
        'Number of features to consider when looking for the best split',
        options=['auto', 'sqrt', 'log2'])
    N_Estimators = st.sidebar.slider('Estimators', 1, 100)
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    model = BalancedRandomForestClassifier(n_estimators=N_Estimators, random_state=Random_State_Seed, max_features=features)
    model.fit(X_train, y_train)

    # Calculate predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))

    # Print the classification report
    from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot Feature Importance
    st.subheader("Feature Importance")
    fig = plt.figure(figsize=(10,10))
    plt.barh(X_train.columns, model.feature_importances_)
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')
    plt.title('Feature Importance')
    st.pyplot(fig)

    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_train.corr(), annot=False)
    st.pyplot(fig)

    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

elif classifier_name == "AdaBoost Classifier":
    st.write("Model: AdaBoost Classifier")

    # Train the AdaBoost Classifier model using the training set
    from imblearn.ensemble import EasyEnsembleClassifier
    strategy = st.sidebar.select_slider(
        'Select a sampling strategy',
        options=['auto', 'majority', 'not minority', 'not majority', 'all'])
    N_Estimators = st.sidebar.slider('Estimators', 1, 100)
    Random_State_Seed = st.sidebar.number_input('Random State Seed', 1, 100, value=1)
    model = EasyEnsembleClassifier(n_estimators=N_Estimators, random_state=Random_State_Seed, sampling_strategy=strategy)
    model.fit(X_train, y_train)

    # Calculate predictions
    y_pred = model.predict(X_test)

    # Calculate the accuracy score
    from sklearn.metrics import balanced_accuracy_score
    balanced_accuracy_score(y_test,y_pred)
    st.write("Balanced Accuracy Score: ", balanced_accuracy_score(y_test,y_pred))

    # Print the classification report
    from imblearn.metrics import classification_report_imbalanced
    from sklearn import metrics
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    df_classification_report = pd.DataFrame(report).transpose()
    df_classification_report = df_classification_report.sort_values(by=['f1-score'], ascending=False)
    st.subheader("Classification Report")
    st.write(df_classification_report)

    # Plot correlation matrix
    st.subheader("Correlation Matrix")
    fig = plt.figure(figsize=(10,10))
    sns.heatmap(X_train.corr(), annot=False)
    st.pyplot(fig)

    # Plot confusion matrix
    st.subheader("Confusion Matrix")
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
    st.pyplot(fig)

