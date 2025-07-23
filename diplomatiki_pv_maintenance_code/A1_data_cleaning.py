# Παράρτημα Α.1 - Καθαρισμός Δεδομένων με τη μεθοδολογία DQRs
# Περιλαμβάνει όλα τα βήματα του DQRs και αποθήκευση καθαρισμένου dataset

import pandas as pd

# ΒΗΜΑ 1 – Φόρτωση δεδομένων και μετατροπή της χρονικής στήλης
column_names = ["time", "P", "G(i)", "H_sun", "T2m", "WS10m", "Int"]
df = pd.read_csv("Timeseries_39.364_22.938_SA3_1kWp_crystSi_14_35deg_0deg_2023_2023.csv",
                 skiprows=11,
                 skipfooter=15,
                 engine="python",
                 names=column_names,
                 sep=",")

df["time"] = pd.to_datetime(df["time"], format="%Y%m%d:%H%M")

# ΒΗΜΑ 2 – Έλεγχος χρονικής συνέπειας
df["time_diff"] = df["time"].diff()
gaps = df[df["time_diff"] > pd.Timedelta(hours=1)]
duplicates = df[df.duplicated(subset="time", keep=False)]

# ΒΗΜΑ 3 – Φιλτράρισμα ωρών ημέρας (G(i) από 20 έως 1300)
df_filtered = df[(df["G(i)"] >= 20) & (df["G(i)"] <= 1300)].copy()

# ΒΗΜΑ 4 – Έλεγχος φυσικών ορίων & αφαίρεση ακραίων τιμών (Boxplot rule)
limits = {
    "P": (0, 1500),
    "G(i)": (0, 1300),
    "H_sun": (0, 90),
    "T2m": (-20, 60),
    "WS10m": (0, 40)
}
for col, (low, high) in limits.items():
    df_filtered = df_filtered[(df_filtered[col] >= low) & (df_filtered[col] <= high)]

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df_filtered = remove_outliers_iqr(df_filtered, "T2m")
df_filtered = remove_outliers_iqr(df_filtered, "WS10m")

# Αποθήκευση του καθαρισμένου dataset (προαιρετικό)
df_filtered.to_excel("cleaned_data_after_step4.xlsx", index=False)

# ΒΗΜΑ 5 – Έλεγχος για απουσίες (NaN / NaT)
missing_counts = df_filtered.isna().sum()
missing_percent = (missing_counts / len(df_filtered)) * 100
missing_report = pd.DataFrame({
    "Missing Values": missing_counts,
    "Missing %": missing_percent.round(2)
})
rows_with_multiple_nans = df_filtered[df_filtered.isna().sum(axis=1) > 1]

if "time_diff" not in df_filtered.columns:
    df_filtered["time"] = pd.to_datetime(df_filtered["time"])
    df_filtered["time_diff"] = df_filtered["time"].diff()

# ΒΗΜΑ 6 – Επιβεβαίωση εγκυρότητας βασικών στηλών
essential_cols = ["time", "P", "G(i)", "H_sun", "T2m", "WS10m", "Int"]
print("Missing values στις βασικές στήλες:
")
print(df_filtered[essential_cols].isna().sum())

# ΒΗΜΑ 7 – Ομαδοποίηση σε μηνιαία βάση
df_filtered["time"] = pd.to_datetime(df_filtered["time"])
df_filtered.set_index("time", inplace=True)
columns_to_aggregate = ["P", "G(i)", "H_sun", "T2m", "WS10m", "Int"]
monthly_data = df_filtered[columns_to_aggregate].resample("M").mean()
monthly_data.reset_index(inplace=True)
monthly_data.to_excel("monthly_data_after_step7.xlsx", index=False)

# ΒΗΜΑ 8 – Περιγραφική στατιστική ανάλυση (ωριαία και μηνιαία)
hourly_stats = df_filtered[columns_to_aggregate[:-1]].describe().round(2)
hourly_stats.to_excel("hourly_stats_output.xlsx")

monthly_stats = monthly_data[columns_to_aggregate[:-1]].describe().round(2)
monthly_stats.to_excel("monthly_stats_output.xlsx")

