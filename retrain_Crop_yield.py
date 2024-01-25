
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pickle
warnings.filterwarnings('ignore')

def Crop_yel():
    data = pd.read_csv('crop_yield.csv')

    columns = ['Crop', 'Season', 'State']
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    for col in columns:
        data[col] = encoder.fit_transform(data[col])

    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 42, test_size= 0.2)

    from sklearn.ensemble import ExtraTreesRegressor
    from sklearn.metrics import r2_score

    model = ExtraTreesRegressor(
        n_estimators=200,
        criterion='squared_error',  
        max_depth=20,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features=5,
        bootstrap=True,
        random_state=42
    )


    model.fit(X_train, y_train)
    pickle.dump(model,open('crop_yield_model.pkl','wb'))


