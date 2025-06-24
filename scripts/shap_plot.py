#!/usr/bin/env python
import shap, pandas as pd, pickle, sys
model = pickle.load(open(sys.argv[1], 'rb'))
data = pd.read_csv(sys.argv[2], sep="\t", index_col=0)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(data.iloc[:, :-n_meta])
shap.summary_plot(shap_values, data.iloc[:, :-n_meta], show=False)
import matplotlib.pyplot as plt; plt.savefig(sys.argv[3])
