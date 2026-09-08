import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Starting model training process...")

#-----------------Data simulation-----------------
# Here I simulate a dataset for demonstration purposes.  
data = {
    'text': [
        "Please review the annual financial report and budget.",
        "The new employee onboarding guide and health insurance forms are ready.",
        "Server downtime scheduled for database migration and security patching.",
        "Quarterly revenue and profit margins exceeded expectations.",
        "Submit your annual leave and vacation requests to management.",
        "Deploying the new REST API endpoints to the production server."
    ],
    'category': ['Finance', 'HR', 'IT', 'Finance', 'HR', 'IT']
}
df = pd.DataFrame(data)

#------------------Data Preprocessing-----------------
# Here you can add any data cleaning or preprocessing steps if needed. For this example, we will proceed directly to vectorization.
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['category']

#------------------Model Training-----------------
print("Training Logistic Regression model...")
model = LogisticRegression()
model.fit(X, y)

#------------------Model Serialization-----------------
# Save the trained model and vectorizer to disk for later use as API endpoints.
os.makedirs('model_assets', exist_ok=True)
joblib.dump(model, 'model_assets/classifier.joblib')
joblib.dump(vectorizer, 'model_assets/vectorizer.joblib')

print("Success! Model and Vectorizer saved in 'model_assets/' directory.")