from sklearn.metrics import *

# Setting up Sample Data
actual_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
predicted_a = [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
#print(actual_a)
#print(predicted_a)

# Confusion Matrix
print("Confusion Matrix \n", confusion_matrix(actual_a, predicted_a))

#Accuracy, precision, recall & F1-Score
print("Accuracy: ", accuracy_score(actual_a, predicted_a))
print("Precision: ", precision_score(actual_a, predicted_a))
print("Recall: ", recall_score(actual_a, predicted_a))
print("F1 Score A:", f1_score(actual_a, predicted_a))
 
#Precision-Recall Curve
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(actual_a, predicted_a)
plt.step(recall, precision, color='g', alpha=0.2, where='post')
plt.fill_between(recall, precision, alpha=0.2, color='g', step='post')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.0])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall curve')
plt.show()