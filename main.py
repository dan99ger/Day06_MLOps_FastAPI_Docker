import joblib
import numpy as np
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 1. تهيئة تطبيق FastAPI
app = FastAPI(
    title="ML Model Serving API",
    description="FastAPI Service for Machine Learning Model Predictions",
    version="1.0.0"
)

# 2. تحميل النموذج عند بدء الخدمة
MODEL_PATH = "../Day02_Machine_Learning_Pipeline/artifacts/best_xgboost_model.joblib"

# في حال عدم وجود نموذج اليوم الثاني في المسار المباشر، نضع خطة بديلة
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

# 3. تحديد شكل البيانات المدخلة باستخدام Pydantic
class ModelInput(BaseModel):
    Age: float = Field(..., example=30.0)
    Salary: float = Field(..., example=60000.0)
    Experience_Years: float = Field(..., example=5.0)
    Department_HR: float = Field(..., example=1.0)
    Department_IT: float = Field(..., example=0.0)
    Department_Sales: float = Field(..., example=0.0)

# 4. مسار الفحص والتحقق (Health Check Endpoint)
@app.get("/")
def health_check():
    return {"status": "online", "model_loaded": model is not None}

# 5. مسار التوقع (Prediction Endpoint)
@app.post("/predict")
def predict(input_data: ModelInput):
    if model is None:
        raise HTTPException(status_code=500, detail="النموذج غير متوفر في المسار المحدد")
    
    # تحويل البيانات إلى مصفوفة NumPy
    features = np.array([[
        input_data.Age,
        input_data.Salary,
        input_data.Experience_Years,
        input_data.Department_HR,
        input_data.Department_IT,
        input_data.Department_Sales
    ]])

    # إجراء التوقع والاحتمالية
    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    return {
        "prediction": prediction,
        "probability_class_1": round(probability, 4),
        "status": "success"
    }