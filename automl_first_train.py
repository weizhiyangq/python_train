# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:50:31 2019

@author: YWZQ
"""

from auto_ml import Predictor
from auto_ml.utils import get_boston_dataset
import numpy as np

from auto_ml.utils_models import load_ml_model
 
df_train, df_test = get_boston_dataset()
#df_train.iloc[1,:]=np.nan
print(df_train.info())


column_descriptions = {
  'MEDV': 'output'
  , 'CHAS': 'categorical'
}
 
ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)
 
ml_predictor.train(df_train)
 
test_score = ml_predictor.score(df_test, df_test.MEDV)
file_name = ml_predictor.save()
 
trained_model = load_ml_model(file_name)
predictions = trained_model.predict(df_test)
#print(predictions)

train_target_pre = df_train[['MEDV']]
train_predictions = trained_model.predict(df_train)
train_target_pre['pre'] = train_predictions
print(train_target_pre.head(100))