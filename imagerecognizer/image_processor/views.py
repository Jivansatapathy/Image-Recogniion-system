from django.shortcuts import render
from .forms import UploadImageForm
from .models import UploadedImage
from .ml_model import process_image
from PIL import Image
from .forms import CropRecommendationForm

def process_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.save()
            

            image_path = uploaded_image.image.path
            result,confidence = process_image(image_path)  # Process the image
            # uploaded_image.classification_result = str(result)

            # Display the uploaded image using Django's ImageField
            image = uploaded_image.image

            return render(request, 'image_processor/result.html', {'result': result, 'image': image, 'confidence':confidence})
    else:
        form = UploadImageForm()
        return render(request, 'image_processor/upload.html', {'form': form})

def home(request):
    return render(request, 'image_processor/index.html')

def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_processor/image_list.html', {'images': images})


def services(request):
    return render(request, 'image_processor/services.html')

def crop(request):
    return render(request, 'image_processor/services.html')

def crop_recommendation(request):
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            recommendation = form.save(commit=False)
            
            # Perform crop recommendation logic based on the input data
            # You'll need to implement this logic based on your requirements
            # For now, I'll assume you have a function called recommend_crop
            recommendation.result = recommend_crop(recommendation)
            recommendation.save()

            return render(request, 'result.html', {'recommendation': recommendation})
    else:
        form = CropRecommendationForm()

    return render(request, 'crop_recommendation.html', {'form': form})

def fertilizer(request):
    return render(request, 'image_processor/services.html')