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
    Variables input:
    estimator: Objeto del Modelo entrenado 
    X: Data Frame con el cual fue entrenado el modelo
    Output:
    score: valor de la métrica silueta
    
    '''
    labels = estimator.fit_predict(X)
    try:
        score = sklearn.metrics.silhouette_score(X, labels, metric='euclidean')
    except ValueError:
        score = -1
    return score

def lecture_data(i):
    '''
    Función que da formato a los archivos que se descargan del INEGI
    Variables input:
    i : Archivo csv que se lee a través de un for
    Variables output:
    denue: ARchivo final csv formateado correctamente 
    '''
    denue = pd.read_csv(i, 
                    index_col=0, 
                    sep ='|',
                    error_bad_lines=False,
                    encoding='latin-1',
                    quoting=csv.QUOTE_NONE)
    return denue
