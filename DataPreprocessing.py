import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = {
    "Name": ["A", "B", "C", "D", None],
    "Age": [25, None, 30, 22, 28],
    "Gender": ["F", "M", "M", "M", "F"],
    "Salary": [50000, 60000, None, 45000, 52000]
}

df = pd.DataFrame(data)

# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Name"].fillna("Unknown", inplace=True)

# Label Encoding
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])
df["Name"] = le.fit_transform(df["Name"])

# Standard Scaling
scaler = StandardScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])

print(df)
