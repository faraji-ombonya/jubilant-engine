import pickle
import pandas as pd
import numpy as np
from django.conf import settings
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


class ConsultantManager():
    def __init__(self):
        self.base_dir = settings.BASE_DIR
        self.consultant_v1 = pickle.load(
            open(str(self.base_dir) + "/consultant_v1.pkl", "rb"))
        print(f"Consultant: {self.consultant_v1}")

    def to_data_frame(self, answer):

        df = pd.DataFrame({
            "BMI": answer.bmi,
            "Smoking": answer.smoking,
            "AlcoholDrinking": answer.alcohol_drinking,
            "Stroke": answer.stroke,
            "PhysicalHealth": answer.physical_health,
            "MentalHealth": answer.mental_health,
            "DiffWalking": answer.diff_walking,
            "Sex": answer.sex,
            "AgeCategory": answer.age_category,
            "Race": answer.race,
            "Diabetic": answer.diabetic,
            "PhysicalActivity": answer.physical_activity,
            "GenHealth": answer.gen_health,
            "SleepTime": answer.sleep_time,
            "Asthma": answer.asthma,
            "KidneyDisease": answer.kidney_disease,
            "SkinCancer": answer.skin_cancer
        }, index=[0])

        return df

    def to_binary_features(self, df):
        df["Smoking"] = df["Smoking"].replace({"Yes": 1, "No": 0})
        df["AlcoholDrinking"] = df["AlcoholDrinking"].replace({"Yes": 1, "No": 0})
        df["Stroke"] = df["Stroke"].replace({"Yes": 1, "No": 0})
        df["DiffWalking"] = df["DiffWalking"].replace({"Yes": 1, "No": 0})
        df["Sex"] = df["Sex"].replace({"Male": 1, "Female": 0})
        df["PhysicalActivity"] = df["PhysicalActivity"].replace({"Yes": 1, "No": 0})
        df["Asthma"] = df["Asthma"].replace({"Yes": 1, "No": 0})
        df["KidneyDisease"] = df["KidneyDisease"].replace({"Yes": 1, "No": 0})
        df["SkinCancer"] = df["SkinCancer"].replace({"Yes": 1, "No": 0})
        print(f"Binary features:")
        print(df)
        return df

    def to_numbers(self, binary_features):
        categorical_features = ["Diabetic", "Race", "GenHealth", "AgeCategory"]
        one_hot = OneHotEncoder()
        transformer = ColumnTransformer(
            [("one_hot", one_hot, categorical_features)],
            remainder="passthrough"
        )

        t_X = transformer.fit_transform(binary_features)

        print(f"Transformed X: {t_X}")
        return t_X

    def predict(self, t_X):
        y_pred = self.consultant_v1.predict(t_X)
        return y_pred
