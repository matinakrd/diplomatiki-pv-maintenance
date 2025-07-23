# diplomatiki-pv-maintenance

Κώδικας διπλωματικής εργασίας: **Προληπτική Συντήρηση Φωτοβολταϊκών με Τεχνητή Νοημοσύνη**

Η εργασία αυτή εστιάζει στην ανάπτυξη και αξιολόγηση μοντέλων τεχνητής νοημοσύνης για την πρόβλεψη της ισχύος παραγωγής και την έγκαιρη ανίχνευση πιθανών βλαβών σε φωτοβολταϊκά συστήματα.

## Περιεχόμενα φακέλου

| Αρχείο                             | Περιγραφή |
|----------------------------------|-----------|
| `A1_data_cleaning.py`            | Καθαρισμός και προεπεξεργασία των αρχικών χρονοσειρών από το PVGIS σύμφωνα με τη μεθοδολογία DQRs. |
| `A2_power_prediction_model.py`   | Εκπαίδευση μοντέλου πρόβλεψης ισχύος (Linear Regression) βάσει των καθαρισμένων δεδομένων. |
| `A3_fault_injection.py`          | Δημιουργία τεχνητών βλαβών και ετικετών (labels) για σκοπούς ταξινόμησης. |
| `A4_logistic_regression_fault_prediction.py` | Εκπαίδευση μοντέλου λογιστικής παλινδρόμησης για την πρόβλεψη παρουσίας βλάβης. Περιλαμβάνει και εξισορρόπηση δεδομένων με SMOTE. |
| `A5_randomforest_xgboost.py`     | Εναλλακτικοί αλγόριθμοι ταξινόμησης (Random Forest & XGBoost) και σύγκριση απόδοσης με τη λογιστική παλινδρόμηση. |
| `README.md`                      | Το παρόν αρχείο τεκμηρίωσης. |

## Περιβάλλον και Βιβλιοθήκες

Η υλοποίηση πραγματοποιήθηκε σε Python 3.11 με χρήση των ακόλουθων βιβλιοθηκών:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `imblearn`
- `xgboost`

Για την αναπαραγωγή των αποτελεσμάτων συνιστάται η εκτέλεση σε περιβάλλον Jupyter Notebook ή άλλο IDE με υποστήριξη Python.

## Εκτέλεση

Η προτεινόμενη σειρά εκτέλεσης των αρχείων είναι η εξής:

1. `A1_data_cleaning.py` – καθαρισμός δεδομένων
2. `A2_power_prediction_model.py` – εκπαίδευση μοντέλου πρόβλεψης ισχύος
3. `A3_fault_injection.py` – εισαγωγή τεχνητών βλαβών
4. `A4_logistic_regression_fault_prediction.py` – πρόβλεψη βλαβών με logistic regression
5. `A5_randomforest_xgboost.py` – δοκιμή εναλλακτικών αλγορίθμων

## Σημειώσεις

- Τα δεδομένα αντλήθηκαν από το PVGIS (Photovoltaic Geographical Information System).
- Ο πλήρης τεκμηριωμένος κώδικας παρατίθεται και στο Παράρτημα της διπλωματικής εργασίας.
- Η εργασία εκπονήθηκε στο πλαίσιο του Τμήματος Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών του Πανεπιστημιού Θεσσαλίας.

# **English Version**

**Code repository for the thesis:** *Predictive Maintenance of Photovoltaics using Artificial Intelligence.*

This project focuses on developing and evaluating AI-based models for power output forecasting and early fault detection in photovoltaic systems.

---

## Repository Contents

| File                              | Description |
|----------------------------------|-------------|
| `A1_data_cleaning.py`            | Data cleaning and preprocessing of time-series data from PVGIS, using the DQRs methodology. |
| `A2_power_prediction_model.py`   | Power prediction model (Linear Regression) trained on the cleaned dataset. |
| `A3_fault_injection.py`          | Fault injection and labeling for classification purposes. |
| `A4_logistic_regression_fault_prediction.py` | Logistic Regression model for fault prediction, including class balancing via SMOTE. |
| `A5_randomforest_xgboost.py`     | Alternative classifiers (Random Forest & XGBoost) and performance comparison with logistic regression. |
| `README.md`                      | This documentation file. |

---

## Environment & Libraries

Developed using Python 3.11 with the following libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `imblearn`
- `xgboost`

For reproducibility, it is recommended to use Jupyter Notebook or any Python IDE.

---

## Execution Steps

1. `A1_data_cleaning.py` – data cleaning
2. `A2_power_prediction_model.py` – training the power prediction model
3. `A3_fault_injection.py` – fault injection
4. `A4_logistic_regression_fault_prediction.py` – logistic regression fault detection
5. `A5_randomforest_xgboost.py` – alternative classifiers and comparison

---

##  Notes

- Data sourced from PVGIS (Photovoltaic Geographical Information System).
- The fully documented code is also included in the thesis appendix.
