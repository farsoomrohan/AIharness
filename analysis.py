import json
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt

with open('alexandrainst_tested_twitter_data.json', 'r') as file:
    data = json.load(file)

y_true = np.array([item['original_score'] for item in data])
y_scores = np.array([item['model_score'] for item in data])

threshold = 0.5
y_pred = np.where(y_scores >= threshold, 1, 0)


accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)
conf_matrix = confusion_matrix(y_true, y_pred).tolist()  
fpr, tpr, thresholds = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

analysis_results = {
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'f1_score': f1,
    'confusion_matrix': conf_matrix,
    'roc_auc': roc_auc,
    'roc_curve': {
        'fpr': fpr.tolist(),  
        'tpr': tpr.tolist(), 
        'thresholds': thresholds.tolist() 
    }
}

with open('alexandrainst_analysis_results.json', 'w') as outfile:
    json.dump(analysis_results, outfile, indent=4)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
roc_curve_path = 'alexandrainst_roc_curve.png'
plt.savefig(roc_curve_path) 
plt.show()

print(f"Analysis results saved to analysis_results.json. ROC curve plot saved to {roc_curve_path}.")

