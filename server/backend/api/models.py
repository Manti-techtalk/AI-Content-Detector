from django.db import models

# Create your models here.

class TextPrediction(models.Model):
    input_text = models.TextField(max_length=5000, verbose_name="Input Text",null=False,blank=False)
    prediction = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{'AI' if self.is_ai else 'Human'} - {self.predicted_at.date()}"
