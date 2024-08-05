from django import forms
from .models import UploadedImage, CropRecommendation, FertilizerRecommendation

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']


class CropRecommendationForm(forms.ModelForm):
    class Meta:
        model = CropRecommendation
        fields = ['nitrogen', 'patassium', 'calcium', 'temperature', 'humidity', 'ph', 'rainfall']
