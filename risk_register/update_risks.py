import pandas as pd
from datetime import datetime

file_path = "risk_register/risk_register.csv"

df = pd.read_csv(file_path)
df["Last_Updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df.to_csv(file_path, index=False)

print("✅ Risk Register updated successfully at", datetime.now())
