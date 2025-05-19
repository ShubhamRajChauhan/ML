#SEVEN 

#Implementing Supervised and Unsupervised Learning
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=200, n_features=4, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

svm = SVC(kernel='linear', probability=True)
svm.fit(X_train, y_train)
svm_accuracy = accuracy_score(y_test, svm.predict(X_test))
print(f"SVM Accuracy: {svm_accuracy: .2f}")

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans_accuracy = accuracy_score(y_test, kmeans.fit_predict(X_test))
print(f"KMeans Accuracy: {kmeans_accuracy: .2f}")







#Implementing Semi-supervised and Reinforcement Learning
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.semi_supervised import SelfTrainingClassifier
import random
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=200, n_features=4, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

y_train_semi = np.copy(y_train)
y_train_semi[np.random.rand(len(y_train_semi)) < 0.3] = -1
semi_supervised = SelfTrainingClassifier(SVC(kernel='linear', probability=True))
semi_supervised.fit(X_train, y_train_semi)
print(f"Semi-supervised Accuracy: {accuracy_score(y_test, semi_supervised.predict(X_test)): .2f}")

actions = [random.choice([0,1]) for _ in range(len(X_test))]
print(f"Reinforcement Accuracy: {accuracy_score(y_test, actions): .2f}")