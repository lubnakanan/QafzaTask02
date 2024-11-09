import uvicorn
from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel

# Define the IDRequest schema
class IDRequest(BaseModel):
    id: int

app = FastAPI()

# Load the CSV file containing predictions
csv_path = r"C:\Users\User\Desktop\Qafza\Task02App\simple xgboost.csv"
data = pd.read_csv(csv_path)

@app.get('/')
def index():
    return {'message': 'XGBoost Model API'}

@app.post('/predict')
def predict(data: IDRequest):
    # Extract the ID from the request
    requested_id = data.id

    # Find the prediction for the given ID
    matching_row = data[data['id'] == requested_id]
    
    if matching_row.empty:
        raise HTTPException(status_code=404, detail="ID not found")

    prediction = matching_row['Target'].values[0]
    return {
        'id': requested_id,
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
