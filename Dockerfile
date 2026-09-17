# 1. صورة قاعدة Python خفيفة
FROM python:3.11-slim

# 2. تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# 3. نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. نسخ كود التطبيق والنموذج
COPY main.py .
# نسخ ملف النموذج من اليوم الثاني إلى داخل الحاوية
COPY artifacts/best_xgboost_model.joblib ./artifacts/best_xgboost_model.joblib

# تعديل متغير المسار في البيئة إن لزم الأمر
ENV MODEL_PATH="./artifacts/best_xgboost_model.joblib"

# 5. فتح المنفذ 8000
EXPOSE 8000
# 6. أمر تشغيل التطبيق عبر Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]