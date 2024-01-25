#!/usr/bin/env python
# coding: utf-8

# In[145]:


from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
import pandas as pd


# In[146]:


data = pd.read_csv('insurance.csv')
data_new = data.copy(deep = True)


# In[147]:


data.head()


# In[148]:


data.isnull().sum()


# In[149]:


data.dropna(inplace = True)


# In[150]:


X = data.drop('gross_premium', axis = 1)
y = data['gross_premium']


# In[151]:


import re

obj_columns = list(data.select_dtypes("object").columns)
obj_columns


# In[152]:


import re

for col in obj_columns:
    data[col] = data[col].astype("str")
    data[col] = data[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9]', '', x.lower())).astype("str")


# In[153]:


season_catogory = list(data.season.values)
scheme_catogory = list(data.scheme.values)
state_catogory  = list(data.state_name.values)
district_catogory = list(data.district_name.values)


# In[154]:


columns = ['season','scheme','state_name','district_name']
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in columns:
    data[col] = encoder.fit_transform(data[col])


# In[155]:


season_label = list(data.season.values)
scheme_label = list(data.scheme.values)
state_label = list(data.state_name.values)
district_label = list(data.district_name.values)


# In[156]:


season_category_label_dict = dict(zip(season_catogory, season_label))

scheme_category_label_dict = dict(zip(scheme_catogory, scheme_label))

state_category_label_dict = dict(zip(state_catogory, state_label))

district_category_label_dict = dict(zip(district_catogory, district_label))


# In[157]:



# In[163]:


# X = data.iloc[:,:-1]
# y = data.iloc[:,-1]


# In[164]:


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# # In[165]:


# from sklearn.linear_model import LinearRegression


# In[166]:


# model = LinearRegression()


# # In[167]:


# model.fit(X, y)


# In[168]:


# import pickle as pk
# filename= 'crop_grosspremimum_Jp.pkl'
# pk.dump(model,open(filename,'wb'))


# In[169]:


def encoding(input_data):
      input_data[0] = season_category_label_dict[input_data[0].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[1] = scheme_category_label_dict[input_data[1].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[2] = state_category_label_dict[input_data[2].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[3] = district_category_label_dict[input_data[3].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      return input_data


# In[170]:


# crop_grosspremimum = pk.load(open(filename, "rb"))


# # In[172]:


# data = ["kharif","PMFBY","Andhra Pradesh","Chittoor",18.82,22410.65,792.39,50.93,50.93,614]
# crop_grosspremimum.predict([encoding(data)])[0]


# In[ ]:




