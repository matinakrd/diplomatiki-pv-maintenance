# Παράρτημα Α.5 - Δοκιμή Random Forest και XGBoost για Πρόβλεψη Βλαβών


Random Forest:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# 1. Φόρτωση δεδομένων
df = pd.read_excel("data_with_simulated_faults.xlsx")

# 2. Επιλογή χαρακτηριστικών και ετικέτας
X = df[["G(i)", "H_sun", "T2m", "WS10m"]]
y = df["fault_label"]

# 3. Διαχωρισμός σε training και test set με αναλογίες κατηγοριών
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Εξισορρόπηση κατηγοριών με SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 5. Εκπαίδευση Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_resampled, y_train_resampled)

# 6. Προβλέψεις
y_pred_rf = rf_model.predict(X_test)

# 7. Αξιολόγηση
print("Classification Report:\n")
print(classification_report(y_test, y_pred_rf, target_names=["Κανονικό", "Βλάβη"]))
conf_matrix = confusion_matrix(y_test, y_pred_rf)
disp = ConfusionMatrixDisplay(conf_matrix, display_labels=["Κανονικό", "Βλάβη"])
disp.plot(cmap="Blues")
plt.title("Πίνακας Σύγχυσης - Random Forest")
plt.show()

XGBoost:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

# 1. Φόρτωση δεδομένων
df = pd.read_excel("data_with_simulated_faults.xlsx")

# 2. Επιλογή χαρακτηριστικών εισόδου και ετικέτας στόχου
X = df[["G(i)", "H_sun", "T2m", "WS10m"]]
y = df["fault_label"]

# 3. Διαχωρισμός σε training και test set με διατήρηση της αναλογίας (stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Εξισορρόπηση training set με SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 5. Δημιουργία και εκπαίδευση μοντέλου XGBoost
model = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train_resampled, y_train_resampled)

# 6. Πρόβλεψη στο test set
y_pred = model.predict(X_test)

# 7. Αξιολόγηση απόδοσης
print("Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=["Κανονικό", "Βλάβη"]))

# 8. Πίνακας Σύγχυσης
conf_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(conf_matrix, display_labels=["Κανονικό", "Βλάβη"])
disp.plot(cmap="Blues")
plt.title("Πίνακας Σύγχυσης – XGBoost (με SMOTE)")
plt.show()

