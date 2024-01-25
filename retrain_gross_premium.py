def grop():
    from sklearn.ensemble import ExtraTreesRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
    data = pd.read_csv('insurance.csv')
    data_new = data.copy(deep = True)
    data.head()
    data.isnull().sum()
    data.dropna(inplace = True)
    X = data.drop('gross_premium', axis = 1)
    y = data['gross_premium']
    import re

    obj_columns = list(data.select_dtypes("object").columns)
    obj_columns
    import re

    for col in obj_columns:
        data[col] = data[col].astype("str")
        data[col] = data[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9]', '', x.lower())).astype("str")
    data.head()
    season_catogory = list(data.season.values)
    scheme_catogory = list(data.scheme.values)
    state_catogory  = list(data.state_name.values)
    district_catogory = list(data.district_name.values)
    columns = ['season','scheme','state_name','district_name']
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    for col in columns:
        data[col] = encoder.fit_transform(data[col])
    season_label = list(data.season.values)
    scheme_label = list(data.scheme.values)
    state_label = list(data.state_name.values)
    district_label = list(data.district_name.values)
    season_category_label_dict = dict(zip(season_catogory, season_label))

    scheme_category_label_dict = dict(zip(scheme_catogory, scheme_label))

    state_category_label_dict = dict(zip(state_catogory, state_label))

    district_category_label_dict = dict(zip(district_catogory, district_label))
    data.season.value_counts()
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    from sklearn.metrics import r2_score
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f'R2 Score: {round(r2*100, 2)}')
    y_pred = model.predict(X_train)
    r2 = r2_score(y_train, y_pred)
    print(f'R2 Score: {round(r2*100, 2)}')
    # There is no miss prediction hence model is not overfitted.........(i.e if its is overfitted than we use regularzation technique)
    import pickle as pk
    filename= 'crop_grosspremimum_Jp.pkl'
    pk.dump(model,open(filename,'wb'))
    def encoding(input_data):
        input_data[0] = season_category_label_dict[input_data[0].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
        input_data[1] = scheme_category_label_dict[input_data[1].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
        input_data[2] = state_category_label_dict[input_data[2].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
        input_data[3] = district_category_label_dict[input_data[3].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
        return input_data
