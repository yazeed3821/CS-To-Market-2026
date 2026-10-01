import pandas as pd
import numpy as np

print("Generating messy ecommerce data...")

# Creating a dataset with deliberate missing values
data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "age": [25, np.nan, 30, 22, 35, np.nan, 40, 28, 29, 50],
    "purchase_amount": [150.50, 200.00, np.nan, 45.00, 300.75, 120.00, np.nan, 80.00, 210.20, 500.00],
    "category": ["Electronics", "Clothing", "Clothing", "Books", "Electronics", np.nan, "Electronics", "Books", "Clothing", "Electronics"]
}

df = pd.DataFrame(data)
df.to_csv("ecommerce_data.csv", index=False)

print("Saved to ecommerce_data.csv")