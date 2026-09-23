import pandas as pd
import random

print("Generating dataset...")

# Dictionaries for category keywords
it_words = ["server", "database", "firewall", "API", "network router", "hardware", "wifi", "laptop", "monitor", "software"]
hr_words = ["leave request", "health insurance", "onboarding", "payroll", "employee", "manager", "recruitment", "salary", "vacation"]
finance_words = ["budget", "tax report", "revenue", "invoice", "profit", "audit", "money", "stocks", "first quarter", "payment"]

# Sentence templates to combine with keywords
templates = [
    "Please review the {word} immediately.",
    "We need an update regarding the {word}.",
    "The {word} is pending your approval.",
    "Issue reported with the {word}, please fix.",
    "Attached is the new {word} for this quarter.",
    "How are our {word} doing?",
    "Can we talk about the {word}?"
]

data = []

# Generate 600 records (200 per category)
for _ in range(200):
    data.append({"text": random.choice(templates).format(word=random.choice(it_words)), "category": "IT"})
    data.append({"text": random.choice(templates).format(word=random.choice(hr_words)), "category": "HR"})
    data.append({"text": random.choice(templates).format(word=random.choice(finance_words)), "category": "Finance"})

# Convert to dataframe and shuffle the data so the model doesn't memorize the order
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)

# Save to csv
df.to_csv("corporate_tickets.csv", index=False)
print("Done. Saved to corporate_tickets.csv")