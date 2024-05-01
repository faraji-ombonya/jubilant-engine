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
        pd.set_option("future.no_silent_downcasting", True)

        df["Smoking"] = df["Smoking"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["AlcoholDrinking"] = df["AlcoholDrinking"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["Stroke"] = df["Stroke"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["DiffWalking"] = df["DiffWalking"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["Sex"] = df["Sex"].replace(
            {"Male": 1, "Female": 0}).infer_objects(copy=False)
        df["PhysicalActivity"] = df["PhysicalActivity"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["Asthma"] = df["Asthma"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["KidneyDisease"] = df["KidneyDisease"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        df["SkinCancer"] = df["SkinCancer"].replace(
            {"Yes": 1, "No": 0}).infer_objects(copy=False)
        return df

    def to_numbers(self, binary_features):
        categorical_features = ["Diabetic", "Race", "GenHealth", "AgeCategory"]

        diabetic_categories = [
            "No", "Yes", "No, borderline diabetes", "Yes (during pregnancy)"]
        race_categories = ["White", "Hispanic", "Black",
                           "Other", "American Indian/Alaskan Native", "Asian"]
        gen_health_categories = [
            "Good", "Very good", "Fair", "Excellent", "Poor"]
        age_categories = ["18-24", "30-34", "25-29", "70-74", "80 or older",
                          "65-69", "60-64", "75-79", "55-59", "50-54", "45-49", "40-44", "35-39"]

        one_hot = OneHotEncoder(categories=[
                                diabetic_categories, race_categories, gen_health_categories, age_categories])
        transformer = ColumnTransformer(
            [("one_hot", one_hot, categorical_features)],
            remainder="passthrough")

        t_X = transformer.fit_transform(binary_features)
        return t_X

    def predict(self, t_X):
        y_pred = self.consultant_v1.predict(t_X)
        return y_pred
