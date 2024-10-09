from django.shortcuts import render
from .forms import HealthForm
import joblib
import pandas as pd

# load model
model = joblib.load("model/best_svm_model.pkl")


def stroke_predict(request):
    result = None
    if request.method == "POST":
        form = HealthForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data["gender"]
            age = form.cleaned_data["age"]
            hypertension = form.cleaned_data["hypertension"]
            heart_disease = form.cleaned_data["heart_disease"]
            ever_married = form.cleaned_data["ever_married"]
            work_type = form.cleaned_data["work_type"]
            residence_type = form.cleaned_data["residence_type"]
            avg_glucose_level = form.cleaned_data["avg_glucose_level"]
            bmi = form.cleaned_data["bmi"]
            smoking_status = form.cleaned_data["smoking_status"]

            # Predict based on the input
            new_data = pd.DataFrame(
                {
                    "gender": [gender],
                    "age": [age],
                    "hypertension": [hypertension],
                    "heart_disease": [heart_disease],
                    "ever_married": [ever_married],
                    "work_type": [work_type],
                    "Residence_type": [residence_type],
                    "avg_glucose_level": [avg_glucose_level],
                    "bmi": [bmi],
                    "smoking_status": [smoking_status],
                }
            )
            prediction = model.predict(new_data)
            if prediction[0] == 1:
                result = "บุคคลนี้มีความเสี่ยงที่จะเกิดโรคหลอดเลือดสมอง"
            else:
                result = "บุคคลนี้มีความเสี่ยงต่ำที่จะเกิดโรคหลอดเลือดสมอง"
    else:
        form = HealthForm()

    return render(request, "index.html", {"form": form, "result": result})
