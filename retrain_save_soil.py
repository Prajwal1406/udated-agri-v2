import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
def soil_model():

    data = pd.read_csv("Cr3.csv")



    import re

    obj_columns = data.select_dtypes("object")

    for col in obj_columns:
        data[col] = data[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9]', '', x.lower())).astype("str")



    data.head()

    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    data["Plant"] = le.fit_transform(data["Plant"])

    # Assuming 'data' is your DataFrame
    # If 'data' is not defined, make sure to load or create your dataset

    X = data.drop('Plant', axis=1)
    y = data['Plant']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the training and testing sets using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Hyperparameter search for RandomForestClassifier
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    rf_classifier = RandomForestClassifier(random_state=42)
    grid_search =GridSearchCV(rf_classifier, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train_scaled, y_train)

    # Get the best parameters and the best estimator
    best_params = grid_search.best_params_
    best_rf_classifier = grid_search.best_estimator_

    # Fit the final model with the best parameters on the entire dataset
    final_rf_classifier = RandomForestClassifier(**best_params, random_state=42)
    final_rf_classifier.fit(X, y)
    pickle.dump(final_rf_classifier,open('Soli_to_recommandation_model_Raghuu.pkl','wb'))
    # return final_rf_classifier









