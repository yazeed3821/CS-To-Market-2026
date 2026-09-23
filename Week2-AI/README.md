# Smart Document Classifier API (V2)

An Applied Machine Learning project demonstrating the end-to-end lifecycle of an AI model: from data generation and training to backend deployment.

## Architecture
1. **Data Generation:** Synthetic corporate dataset creation using a Python script (`generate_data.py`).
2. **Model Training:** NLP text classification using `scikit-learn` (Logistic Regression + TF-IDF) trained on a scaled CSV dataset.
3. **Serialization:** Model and vectorizer exported as `.joblib` assets.
4. **API Integration:** Served as a functional RESTful endpoint using `FastAPI` and `Uvicorn`.

## Current Status (V2)
* Implemented a data generator to create a 600-record CSV dataset (`corporate_tickets.csv`) covering IT, HR, and Finance terminology.
* Upgraded the training pipeline to read from the CSV, significantly expanding the model's vocabulary and accuracy.
* Deployed the updated model via the `/classify` API endpoint.