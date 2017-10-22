# -*- coding: utf-8 -*-
"""
KMeans for Geometry Parsing
"""

### Import libraries

# importing division from the 'future' release of Python (i.e. Python 3)
from __future__ import division

# importing libraries
import os
import math

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import preprocessing


# PATH: Path starts from root metashape/ML Models
train_path = os.getcwd()
train_path += "/../Results/simpleGeoData.csv"
print train_path

test_path = os.getcwd()
test_path += "/../Results/simpleGeoData2.csv"

# importing database
georaw_train_df = pd.read_csv(train_path)
georaw_test_df = pd.read_csv(test_path)

# creating cross validation
CROSS_VALIDATION_AMOUNT = .2

#################################
# Encoding Categorical Features #
#################################

##################
# Label Encoding #
##################

def encode_merge(data_frame):
    string_features = data_frame.ix[:, data_frame.dtypes == 'object'] #data inside is string data if object, all rows
    numeric_features = data_frame.ix[:, data_frame.dtypes != 'object']

    string_features = string_features.fillna('Nothing')

    encoded_data = pd.DataFrame(index = string_features.index) # empty data frame

    le = preprocessing.LabelEncoder()
    for col in string_features.columns:
        uniq_strings = pd.Series(le.fit_transform(string_features[col]), name=col+"_cat")
        encoded_data = pd.concat([encoded_data, uniq_strings], axis=1)

    geo_df = pd.concat([numeric_features, encoded_data], axis = 1)
    return string_features, numeric_features, geo_df

train_string, train_numeric, train_df = encode_merge(georaw_train_df)
test_string, test_numeric, test_df = encode_merge(georaw_test_df)

print "Training!"
print train_df
# ###########
# # Merging #
# ###########
#
# print "Merging!"
# geo_df = pd.concat([numeric_features, encoded_data], axis = 1)
# print geo_df.head()

######################
# Training + Testing #
######################

# # separating response variable from your explanatory variables
response_header = ['Shape_cat']
response_series = test_df[response_header]

explanatory_header = [col for col in train_df.columns if col not in response_header]
explanatory_test = test_df[explanatory_header]

print explanatory_test

response_train = train_df[response_header]
explanatory_train = train_df[explanatory_header]

# # setting up testing and training sets
# # hold out indices
# holdout_num = round(len(geo_df.index) * CROSS_VALIDATION_AMOUNT, 0)
#
# test_indices = np.random.choice(geo_df.index, holdout_num, replace = False )
# train_indices = geo_df.index[~geo_df.index.isin(test_indices)]
#
# response_train = response_series.ix[train_indices,]
# explanatory_train = explanatory_variables.ix[train_indices,]
#
# response_test = response_series.ix[test_indices,]
# explanatory_test = explanatory_variables.ix[test_indices,]
######################
# KNN Classification #
######################
KNN_classifier = KNeighborsClassifier(n_neighbors=3, p = 2)
print explanatory_train
print response_train
KNN_classifier.fit(explanatory_train, response_train)

predicted_response = KNN_classifier.predict(explanatory_test)
# print predicted_response
