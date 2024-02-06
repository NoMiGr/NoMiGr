
from sklearn.metrics import accuracy_score
import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from scipy.stats import entropy
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz
from sklearn.tree import export_graphviz
import pydotplus

df = pd.read_csv ('train_data_tree.csv')

X = df[['sex', 'exang']]
y = df['num']

# Создание модели Decision Tree с критерием entropy
model = DecisionTreeClassifier(criterion='entropy')

model.fit(X, y)
feature_importances = model.feature_importances_
gain_for_root = feature_importances[0]

# Generate the decision tree visualization
plt.figure(figsize=(10, 8))
tree.plot_tree(model, feature_names=X.columns, class_names=['0', '1'], filled=True, rounded=True)

# Display the decision tree visualization
plt.show()