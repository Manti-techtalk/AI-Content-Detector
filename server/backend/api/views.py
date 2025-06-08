import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from joblib import load
from .serializers import TextPredictionSerializer
from .models import TextPrediction
from dotenv import load_dotenv

load_dotenv()

# Load model once
model_path = os.getenv('path')
model = load(model_path)
class PredictTextAPIView(APIView):
    def post(self, request):
        serializer = TextPredictionSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data['input_text']

            prediction = model.predict([input_text])[0]
            proba = model.predict_proba([input_text])[0]
            confidence = max(proba)

            # Save to DB
            record = TextPrediction.objects.create(
                input_text=input_text,
                prediction=bool(prediction)
            )

            return Response({
                "result": "Human" if prediction else "AI",
                "confidence": round(confidence * 100, 2),
                "id": record.id
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
