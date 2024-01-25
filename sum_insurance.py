
import pandas as pd
import numpy as np



data = pd.read_csv("insurance(R).csv")
data_new = data.copy(deep = True)



data.head()



import re

obj_columns = data.select_dtypes("object")

for col in obj_columns:
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


from sklearn.compose import ColumnTransformer
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, FunctionTransformer
from sklearn.model_selection import train_test_split


X = data.drop("sum_insured", axis=1)
y = data["sum_insured"]


def encoding(input_data):
      input_data[0] = season_category_label_dict[input_data[0].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[1] = scheme_category_label_dict[input_data[1].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[2] = state_category_label_dict[input_data[2].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[3] = district_category_label_dict[input_data[3].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      return input_data



