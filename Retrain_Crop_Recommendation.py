import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder,OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
def crop_reco():


    df = pd.read_csv('Crop_recommendation.csv')

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    df['label'] = le.fit_transform(df['label'])

    class_labels = le.classes_

    x = df.drop('label',axis=1)
    y = df['label']

    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.10,shuffle=True)

    rf = RandomForestClassifier()
    param_grid = {'n_estimators':np.arange(50,200),
        'criterion':['gini','entropy'],
        'max_depth':np.arange(2,25),
        'min_samples_split':np.arange(2,25),
        'min_samples_leaf':np.arange(2,25)}

    rscv_model = RandomizedSearchCV(rf,param_grid, cv=5)
    rscv_model.fit(X_train,y_train)

    best_rf_model = rscv_model.best_estimator_
    pickle.dump(best_rf_model, open("crop_recommendation.pickle","wb"))

