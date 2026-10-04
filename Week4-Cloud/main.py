from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Here we define the FastAPI application and load the trained model and vectorizer for use in the API endpoints.
app = FastAPI(title="Smart Document Classifier API", description="API to classify documents into HR, IT, or Finance")

# Here we load the trained model and vectorizer from disk. This allows us to use them for predictions without retraining.
print("Loading model assets...")
model = joblib.load('model_assets/classifier.joblib')
vectorizer = joblib.load('model_assets/vectorizer.joblib')
print("Model loaded successfully!")

# Here we define a Pydantic model to validate the incoming request data. This ensures that the API receives the expected format.
class DocumentRequest(BaseModel):
    text: str

# This endpoint receives a document text, vectorizes it using the loaded vectorizer, and predicts its category using the trained model. The result is returned in JSON format.
@app.post("/classify")
def classify_document(doc: DocumentRequest):
    # Transform the input text into a vector using the loaded vectorizer
    vectorized_text = vectorizer.transform([doc.text])
    
    # Predict the category using the trained model
    prediction = model.predict(vectorized_text)[0]
    
    # Return the result in JSON format
    return {
        "status": "success",
        "predicted_category": prediction,
        "original_text": doc.text
    }