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
georaw_test_df = pd.read_csv(test_path)
geo_test_values = georaw_test_df.values

# creating cross validation
CROSS_VALIDATION_AMOUNT = .2

#################################
# Encoding Categorical Features #
#################################
string_features = georaw_df.ix[:, georaw_df.dtypes == 'object'] #data inside is string data if object, all rows
numeric_features = georaw_df.ix[:, georaw_df.dtypes != 'object']

string_features = string_features.fillna('Nothing')


##################
# Label Encoding #
##################

encoded_data = pd.DataFrame(index = string_features.index) # empty data frame

le = preprocessing.LabelEncoder()
for col in string_features.columns:
    uniq_strings = pd.Series(le.fit_transform(string_features[col]), name=col+"_cat")
    encoded_data = pd.concat([encoded_data, uniq_strings], axis=1)


######################
# KNN Classification #
######################
KNN_classifier = KNeighborsClassifier(n_neighbors=3, p = 2)
KNN_classifier.fit(explanatory_train, response_train)

predicted_response = KNN_classifier.predict(explanatory_test)
# print predicted_response
