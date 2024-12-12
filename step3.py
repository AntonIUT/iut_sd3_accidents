import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
victime = pd.read_csv('step2/missing_values_deleted.csv', sep=',', encoding='UTF-8',dtype=str)
victime.corr()
victime.var()
victime = victime.drop(columns=['an'])

hrmn=pd.cut(victime['hrmn'],24,labels=[str(i) for i in range(0,24)])
victime['hrmn']=hrmn.values
# On extrait du tableau la latitude et la longitude

X_lat = victime['lat']
X_long = victime['long']

# On définit tous nos points à classifier

X_cluster = np.array((list(zip(X_lat, X_long))))

# Kmeans nous donne pour chaque point la catégorie associée

clustering = KMeans(n_clusters=15, random_state=0)
clustering.fit(X_cluster)

# Enfin on ajoute les catégories dans la base d'entraînement

geo = pd.Series(clustering.labels_)
victime['geo'] = geo
victime[['hrmn', 'month', 'geo']].to_csv('step3/time_encoding.csv', index=False, encoding='UTF-8')
