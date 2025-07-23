# Παράρτημα Α.2 - Εκπαίδευση Μοντέλου Πρόβλεψης Ισχύος
# Χρήση γραμμικής παλινδρόμησης για πρόβλεψη ισχύος με βάση τις περιβαλλοντικές μεταβλητές


# Φόρτωση απαραίτητων βιβλιοθηκών
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_percentage_error

# Φόρτωση του καθαρισμένου dataset
df = pd.read_excel("cleaned_data_after_step4.xlsx")

# Επιλογή μεταβλητών εισόδου και εξόδου
X = df[["G(i)", "H_sun", "T2m", "WS10m"]]  # Ανεξάρτητες μεταβλητές
y = df["P"]                                # Εξαρτημένη μεταβλητή (ισχύς)

# Διαχωρισμός σε σύνολο εκπαίδευσης (80%) και δοκιμής (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Δημιουργία και εκπαίδευση μοντέλου γραμμικής παλινδρόμησης
model = LinearRegression()
model.fit(X_train, y_train)

# Πρόβλεψη ισχύος στο test set
y_pred = model.predict(X_test)

# Υπολογισμός στατιστικών δεικτών απόδοσης
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100

# Εμφάνιση αποτελεσμάτων
print(f" Μέσο Απόλυτο Σχετικό Σφάλμα (MAPE): {mape:.2f}%")
print(f" Συντελεστής Προσδιορισμού (R²): {r2:.4f}")

# Γράφημα: Πραγματική vs Προβλεπόμενη Ισχύς
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, label="Προβλέψεις")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label="Ιδανική Πρόβλεψη")
plt.xlabel("Πραγματική Ισχύς P (W)")
plt.ylabel("Προβλεπόμενη Ισχύς P_pred (W)")
plt.title("Σύγκριση Πραγματικής και Προβλεπόμενης Ισχύος")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Εμφάνιση γραμμικής εξίσωσης πρόβλεψης
print("\n Γραμμική Σχέση Μοντέλου:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Σταθερός Όρος (Intercept): {model.intercept_:.4f}")

