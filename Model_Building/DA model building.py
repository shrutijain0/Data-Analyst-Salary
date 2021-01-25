# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:25:29 2021

@author: milin
"""
#importing all the libraires
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df=pd.read_csv('Cleaned DS data.csv')
df_to_use=df[['Rating','Size','Title_Simplified','Level','job_location','age','num_comp','avg_salary','company_txt','Type of ownership','Industry','Sector','Revenue','Easy Apply']]

#creating dummie for all categorical features
df_model = pd.get_dummies(df_to_use)
df_model=df_model.fillna(0)


X=df_model.drop('avg_salary',axis=1)
y=df_model.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#linear regrrion model building
reg=LinearRegression()

reg.fit(X_train,y_train)

#random forest model building'
classifier = RandomForestRegressor()
classifier.fit(X_train,y_train)

re_prec=reg.predict(X_test)
ra_prec=classifier.predict(X_test)
#evaluating the accuracy of the models
maer=mean_absolute_error(y_test,re_prec)
maerf=mean_absolute_error(y_test,ra_prec)

#random forest has less MAE score which shows this is more accurate model than linear regression
import pickle
pickl = {'model':classifier }
pickle.dump( pickl, open( 'classifier' + ".p", "wb" ) )

file_name = "classifier.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
