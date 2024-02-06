
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

print("import pandas as pd\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.model_selection import RandomizedSearchCV\nfrom sklearn.datasets import load_iris\nfrom scipy.stats import randint\n\n# Загрузка данных\niris = load_iris()\nX = iris.data\ny = iris.target\n\n# Задаем параметры для перебора\nparams = {'max_depth': randint(1, 11),\n          'min_samples_split': randint(2, 11),\n          'min_samples_leaf': randint(1, 11)}\n\n# Создаем объект классификатора\nclf = DecisionTreeClassifier()\n\n# Создаем объект RandomizedSearchCV с указанными параметрами\nsearch = RandomizedSearchCV(estimator=clf, param_distributions=params)\n\n# Обучаем модель на данных и ищем лучшие параметры\nsearch.fit(X, y)\n\n# Получаем модель с лучшими параметрами\nbest_tree = search.best_estimator_\n\n# Выводим лучшие параметры\nprint(\"Best Parameters: \", search.best_params_)\n\n# Выводим лучшую модель\nprint(\"Best Tree: \", best_tree)\n")


