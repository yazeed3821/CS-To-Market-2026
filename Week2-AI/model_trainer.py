import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Loading dataset...")
# Load the generated dataset
df = pd.read_csv('corporate_tickets.csv')

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['category']

print("Training model...")
# Train the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Create directory and save model files for the API
os.makedirs('model_assets', exist_ok=True)
joblib.dump(model, 'model_assets/classifier.joblib')
joblib.dump(vectorizer, 'model_assets/vectorizer.joblib')

print("Model saved.")