#SIX

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

depths = range(1, 21)
train_accuracies, test_accuracies = zip(*[
    (accuracy_score(y_train, 
DecisionTreeClassifier(criterion='entropy', max_depth=d, 
random_state=42).fit(X_train, y_train).predict(X_train)), 
     accuracy_score(y_test,
DecisionTreeClassifier(criterion='entropy', max_depth=d, 
random_state=42).fit(X_train, y_train).predict(X_test))) 
    for d in depths
])

plt.plot(depths, train_accuracies, label= 'Training Accuracy', marker= 'o')
plt.plot(depths, test_accuracies, label= 'Testing Accuracy', marker= 's')
plt.xlabel('Tree Depth')
plt.ylabel('Accuracy')
plt.title('ID3 Decision Tree Performance')
plt.legend()
plt.show()

