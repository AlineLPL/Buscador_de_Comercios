from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import silhouette_score
from sklearn.model_selection import GridSearchCV,KFold
import pandas as pd
import numpy as np
import os
import csv

def silhouette_score_f(estimator, X):
    '''
    Función que genera la métrica de silueta para modelos de clusters
    estimator: 
    X:
    
    '''
    labels = estimator.fit_predict(X)
    try:
        score = sklearn.metrics.silhouette_score(X, labels, metric='euclidean')
    except ValueError:
        score = -1
    return score

def DBSNC_F():
    '''
    Función que genera la métrica de silueta para modelos de clusters
    estimator: 
    X:
    
    '''
    dbscan = DBSCAN()
    cv = KFold(n_splits=10)
    parameters = {'eps': [0.001,0.01,0.0125,0.02,0.05,0.8,1,1.5],
                  'min_samples': [5,10,15,50]}
    dbscan_gs = GridSearchCV(dbscan, parameters, cv = cv, n_jobs=-1,scoring= silhouette_score_f, error_score=-1)
    
    return dbscan_gs

def lecture_data(i):
    '''
    
    '''
    denue = pd.read_csv(i, 
                    index_col=0, 
                    sep ='|',
                    error_bad_lines=False,
                    encoding='latin-1',
                    quoting=csv.QUOTE_NONE)
    return denue
