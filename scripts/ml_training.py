#!/usr/bin/env python
import pandas as pd, sys, pickle
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
# ...
data = pd.read_csv(sys.argv[1], sep="\t", index_col=0)
X = data.iloc[:, :-n_meta]
y = data["target_column"]
# PCA
pca = PCA(n_components=10).fit(X)
X_pca = pca.transform(X)
# Model
model = RandomForestRegressor(**params).fit(X_pca, y)
pickle.dump(model, open(sys.argv[2], 'wb'))
pd.DataFrame(pca.components_).to_csv(sys.argv[3], sep="\t"
