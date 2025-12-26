from fastapi import FastAPI
from pydantic import BaseModel #-> for input validation
import pickle #-> load trained model

#create fastapi app
app= FastAPI()

#load trained model -> loaded once at startup
with open("student_pass_model.pkl","rb") as file:
    model=pickle.load(file)

#define input schema
class StudentInput(BaseModel):
    hours_studied: int
    attendance: int

#prediction endpoint
@app.post("/predict")
def predict(data: StudentInput):
    # make prediction
    prediction= model.predict([[data.hours_studied, data.attendance]])
    # convert output
    result = "PASS" if prediction[0] ==1 else "FAIL" # prediction[0] -> first element of the array picking because we are only making one prediction
    return { # returning json response
    "prediction": result
   }
