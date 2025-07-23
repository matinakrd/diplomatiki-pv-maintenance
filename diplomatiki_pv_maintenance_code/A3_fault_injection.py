# Παράρτημα Α.3 - Δημιουργία Τεχνητών Βλαβών
# Εισαγωγή τεχνητών βλαβών με τυχαία μείωση ισχύος

import pandas as pd
import numpy as np

# 1. Φόρτωση του αρχείου με τα καθαρισμένα δεδομένα
df = pd.read_excel("cleaned_data_after_step4.xlsx")

# 2. Δημιουργία αντιγράφου για να μην τροποποιηθεί το αρχικό dataset
df_faults = df.copy()

# 3. Δημιουργία νέας στήλης με όνομα fault_label, με αρχική τιμή 0 (φυσιολογική λειτουργία)
df_faults["fault_label"] = 0

# 4. Υπολογισμός του πλήθους των παρατηρήσεων που θα αλλοιωθούν (8% του συνόλου)
n_faults = int(len(df_faults) * 0.08)

# 5. Επιλογή τυχαίων γραμμών για δημιουργία τεχνητών βλαβών, με χρήση σταθερού seed
np.random.seed(42)
fault_indices = np.random.choice(df_faults.index, size=n_faults, replace=False)

# 6. Μείωση της ισχύος P κατά 70% στις επιλεγμένες γραμμές
df_faults.loc[fault_indices, "P"] *= 0.3

# 7. Αντικατάσταση της τιμής στη στήλη fault_label με 1 για τις αλλοιωμένες γραμμές
df_faults.loc[fault_indices, "fault_label"] = 1

# 8. Αποθήκευση του νέου αρχείου σε Excel για χρήση σε επόμενα βήματα
df_faults.to_excel("data_with_simulated_faults.xlsx", index=False)

# 9. Εμφάνιση συνοπτικής πληροφορίας για έλεγχο ορθότητας
print("Ολοκληρώθηκε η εισαγωγή τεχνητών βλαβών.")
print(f"Κανονικά σημεία: {(df_faults['fault_label'] == 0).sum()}")
print(f"Τεχνητές βλάβες: {(df_faults['fault_label'] == 1).sum()}")
