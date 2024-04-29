from rest_framework import serializers
from consultant.models import Answer
from consultant.utils.consultant import ConsultantManager


class AnswerSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):

        m = ConsultantManager()
        df = m.to_data_frame(instance)
        binary_features = m.to_binary_features(df)
        numbers = m.to_numbers(binary_features)
        prediction = m.predict(numbers)

        print(f"Prediction: {prediction}")

        ret = super().to_representation(instance)

    class Meta:
        model = Answer
        fields = '__all__'
