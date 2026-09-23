import pandas as pd
import random

print(" Generating corporate dataset...")

# A list of keywords for each category
it_words = ["server", "database", "firewall", "API endpoints", "network router", "production environment", "login system"]
hr_words = ["leave request", "health insurance", "onboarding document", "payroll", "employee interview", "vacation policy"]
finance_words = ["annual budget", "tax report", "Q3 revenue", "expense invoice", "profit margins", "financial audit"]

# A list of sentence templates to be merged with the keywords

templates = [
    "Please review the {word} immediately.",
    "We need an update regarding the {word}.",
    "The {word} is pending your approval.",
    "Issue reported with the {word}, please fix.",
    "Attached is the new {word} for this quarter."
]

data = []

# Generate 600 documents (200 for each category) for training the model
for _ in range(200):
    data.append({"text": random.choice(templates).format(word=random.choice(it_words)), "category": "IT"})
    data.append({"text": random.choice(templates).format(word=random.choice(hr_words)), "category": "HR"})
    data.append({"text": random.choice(templates).format(word=random.choice(finance_words)), "category": "Finance"})

# Convert the data to a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
# Shuffle the data so the model doesn't learn the order
df = df.sample(frac=1).reset_index(drop=True) 

df.to_csv("corporate_tickets.csv", index=False)
print(f"Success! Generated 'corporate_tickets.csv' with {len(df)} documents.")