# Smart Document Classifier API (V1)

An Applied Machine Learning project demonstrating the end-to-end lifecycle of an AI model: from training to backend deployment.

## Architecture
1. **Model Training:** NLP text classification using `scikit-learn` (Logistic Regression + TF-IDF).
2. **Serialization:** Model and vectorizer exported as `.joblib` assets.
3. **API Integration:** Served as a functional RESTful endpoint using `FastAPI` and `Uvicorn`.

## Current Status (V1)
* Successfully classifies basic text inputs into corporate categories (IT, HR, Finance).
* **Next Phase:** Data scaling with a larger, real-world corporate dataset to improve prediction accuracy on complex documents.