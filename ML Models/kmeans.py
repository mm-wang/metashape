# -*- coding: utf-8 -*-
"""
KNN for Geometry Parsing
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
path = os.getcwd()
path += "/../Results/simpleGeoData2.csv"
print path

# importing database
georaw_df = pd.read_csv(path)
print georaw_df
geo_values = georaw_df.values

# creating cross validation
CROSS_VALIDATION_AMOUNT = .2

# print response_series

#################################
# Encoding Categorical Features #
#################################
string_features = georaw_df.ix[:, georaw_df.dtypes == 'object'] #data inside is string data if object, all rows
numeric_features = georaw_df.ix[:, georaw_df.dtypes != 'object']

string_features = string_features.fillna('Nothing')

## creating catcher data frame that will hold the encoded data
# encoded_data = pd.DataFrame(index = string_features.index) # empty data frame
# for col in string_features.columns:
#     ## calling pandas.get_dummies to turn the column into a sequence of
#     ## binary variables
#     current_data = pd.get_dummies(string_features[col], prefix=col.encode('ascii', 'replace'))
#     # creates dummy variables, can create a prefix - it is the column name
#     encoded_data = pd.concat([encoded_data, current_data], axis=1)
#     # concatenating new dataFrame to encoded dataFrame
#
# def get_binary_values(data_frame):
#     """Encodes categorical features in Pandas with get_dummies.
#     Includes prefix of column name.
#     """
#     all_columns = pd.DataFrame(index = data_frame.index)
#     for col in data_frame.columns:
#         data = pd.get_dummies(data_frame[col], prefix=col.encode('ascii', 'replace'))
#         all_columns = pd.concat([all_columns, data], axis=1)
#     return all_columns
#
# encoded_data = get_binary_values(string_features)
#
# # verify that encoding occurred
# print "Encoded Strings"
# print encoded_data.head()


##################
# Label Encoding #
##################

encoded_data = pd.DataFrame(index = string_features.index) # empty data frame

le = preprocessing.LabelEncoder()
for col in string_features.columns:
    uniq_strings = pd.Series(le.fit_transform(string_features[col]), name=col+"_Cat")
    print list(uniq_strings)
    encoded_data = pd.concat([encoded_data, uniq_strings], axis=1)

###########
# Merging #
###########

print "Merging!"
geo_df = pd.concat([numeric_features, encoded_data], axis = 1)
print geo_df.head()

################
# Scaling Data #
################

scaler = preprocessing.StandardScaler()
scaler.fit(geo_df)
geo_df = pd.DataFrame(scaler.transform(geo_df),
                                  columns = geo_df.columns)

###########################
# Imputing Missing Values #
###########################

from sklearn.preprocessing import Imputer
imputer_object = Imputer(missing_values='NaN', strategy = 'median', axis = 0)
imputer_object.fit(numeric_features)
numeric_features = pd.DataFrame(imputer_object.transform(numeric_features),
                                    columns = numeric_features.columns)

######################
# Training + Testing #
######################

# # separating response variable from your explanatory variables
# response_header = ['Shape']
# response_series = georaw_df[response_header]
#
# explanatory_header = ['Area', 'Volume', 'centroid x', 'centroid y ', \
#     'centroid z', 'BB_Height', 'BB_Width', 'BB_Depth', 'low_slice_length', \
#     'mid_slice_length', 'upper_slice_length']
# explanatory_variables = georaw_df[explanatory_header]
#
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

#####################
# KMeans Clustering #
#####################
kmeans_est = KMeans(n_clusters = 4)
kmeans_est.fit(geo_df);
labels = kmeans_est.labels_

print kmeans_est
print labels

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(geo_df.Shape_Cat, geo_df.Volume, geo_df.Area, s=60, c=labels)

ax.set_xlabel('Shape')
ax.set_ylabel('Volume')
ax.set_zlabel('Area')

plt.show();
######################
# KNN Classification #
######################
# KNN_classifier = KNeighborsClassifier(n_neighbors=3, p = 2)
# KNN_classifier.fit(explanatory_train, response_train)
#
# predicted_response = KNN_classifier.predict(explanatory_test)
# print predicted_response
