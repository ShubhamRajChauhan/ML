#TEN

import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
import matplotlib.pyplot as plt

mnist=fetch_openml('mnist_784',version=1)
x,y=mnist.data/255.0,mnist.target.astype(int)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

binary_mask_train=(y_train==0)|(y_train==1)
binary_mask_test=(y_test==0)|(y_test==1)

x_train_bin,y_train_bin=x_train[binary_mask_train],y_train[binary_mask_train]
x_test_bin,y_test_bin=x_test[binary_mask_test],y_test[binary_mask_test]

model_bin=LogisticRegression(max_iter=1000).fit(x_train_bin,y_train_bin)

y_pred_bin=model_bin.predict(x_test_bin)
print("Binary Classification Report (0vs 1):")
print(classification_report(y_test_bin,y_pred_bin))

model_multi=LogisticRegression(max_iter=1000,multi_class='ovr').fit(x_train,y_train)
y_pred_multi=model_multi.predict(x_test)
print("\nMulticlass Classification Report:")
print(classification_report(y_test,y_pred_multi))

conf_matrix=confusion_matrix(y_test,y_pred_multi)
plt.imshow(conf_matrix,cmap="Blues",interpolation='nearest')
plt.colorbar()
plt.title("Confusion Matrix")
plt.xlabel('True label')
plt.ylabel('Predicted label')
plt.show()