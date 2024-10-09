from django import forms


class HealthForm(forms.Form):
    GENDER_CHOICES = [
        (0, "ชาย"),
        (1, "หญิง"),
        (2, "อื่น ๆ"),
    ]

    YES_NO_CHOICES = [
        (1, "ใช่"),
        (0, "ไม่"),
    ]

    RESIDENCE_CHOICES = [
        (0, "ชนชท"),
        (1, "เมือง"),
    ]

    WORK_CHOICES = [
        (0, "ไม่เคยทำงาน"),
        (1, "ทำงานเอกชน"),
        (2, "อาชีพอิสระ"),
        (3, "นักเรียนหรือนักศึกษา"),
    ]

    SMOKING_CHOICES = [
        (0, "ไม่ทราบ"),
        (1, "เคยสูบมาก่อน"),
        (2, "ไม่เคยสูบ "),
        (3, "สูบ"),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="เพศ")
    age = forms.IntegerField(label="อายุ(ปี)", min_value=0)
    hypertension = forms.ChoiceField(choices=YES_NO_CHOICES, label="มีความดันสูงหรือไม่")
    heart_disease = forms.ChoiceField(choices=YES_NO_CHOICES, label="เป็นโรคหัวใจหรือไม่")
    ever_married = forms.ChoiceField(choices=YES_NO_CHOICES, label="เคยแต่งงานหรือไม่")
    work_type = forms.ChoiceField(choices=WORK_CHOICES, label="ประเภทการทำงาน")
    residence_type = forms.ChoiceField(choices=RESIDENCE_CHOICES, label="แหล่งที่อยู่")
    avg_glucose_level = forms.FloatField(label="ระดับน้ำตาลในเลือดเฉลี่ย", min_value=0)
    bmi = forms.FloatField(label="BMI", min_value=0)
    smoking_status = forms.ChoiceField(choices=SMOKING_CHOICES, label="สูบบุหรี่หรือไม่")
