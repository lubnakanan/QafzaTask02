import uvicorn
from fastapi import FastAPI, HTTPException
from BankUser import BankUser

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Bank User Model API'}

@app.post('/user/predict')
def predict_user(data: BankUser):
    # Here you could implement logic to process the bank user data
    # For example, return the received data or perform predictions
    return {
        'message': 'User data received successfully',
        'data': data.dict()  # Convert Pydantic model to dictionary for response
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)  # Run on a different port
