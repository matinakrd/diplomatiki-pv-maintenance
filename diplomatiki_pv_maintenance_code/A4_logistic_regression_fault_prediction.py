# Παράρτημα Α.4 - Μοντέλο Λογιστικής Παλινδρόμησης για Πρόβλεψη Βλαβών
# Χρήση SMOTE και Logistic Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# Φόρτωση δεδομένων
df = pd.read_excel("data_with_simulated_faults.xlsx")

# Επιλογή χαρακτηριστικών και ετικέτας
X = df[["G(i)", "H_sun", "T2m", "WS10m"]]
y = df["fault_label"]

# Διαχωρισμός σε training και test set με αναλογίες κατηγοριών
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Εξισορρόπηση κατηγοριών με SMOTE (τεχνητά δείγματα)
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Εκπαίδευση μοντέλου λογιστικής παλινδρόμησης
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_resampled, y_train_resampled)

# Προβλέψεις στο test set
y_pred = model.predict(X_test)

# Αξιολόγηση – Αναφορά & Πίνακας Σύγχυσης
print("Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=["Κανονικό", "Βλάβη"]))

conf_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(conf_matrix, display_labels=["Κανονικό", "Βλάβη"])
disp.plot(cmap="Blues")
plt.title("Πίνακας Σύγχυσης (με SMOTE)")
plt.show()
