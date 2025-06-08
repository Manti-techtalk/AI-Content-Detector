from rest_framework import serializers
from api.models import TextPrediction


class TextPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPrediction
        fields = ['input_text']
        read_only_fields = ['id', 'created_at', 'prediction']
        