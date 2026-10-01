import pandas as pd

# Load raw data
df = pd.read_csv("ecommerce_data.csv")

# Clean data
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)
df = df.dropna(subset=['purchase_amount', 'category'])

# Save cleaned data
df.to_csv("cleaned_ecommerce_data.csv", index=False)
print("Cleaned data saved to cleaned_ecommerce_data.csv")
print("-" * 30)

# Business Analysis: Total sales per category
print("Total Sales by Category:")
category_sales = df.groupby('category')['purchase_amount'].sum()
print(category_sales)

print("-" * 30)

# Business Analysis: Average transaction value
print("Average Transaction Value:")
avg_transaction = df['purchase_amount'].mean()
print(round(avg_transaction, 2))