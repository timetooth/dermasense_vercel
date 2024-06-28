from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import numpy as np
import cv2 as cv
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
decoder = {
    0: 'Melanocytic nevi',
    1: 'Melanoma',
    2: 'Benign keratosis-like lesions',
    3: 'Basal cell carcinoma',
    4: 'Actinic keratoses',
    5: 'Vascular lesions',
    6: 'Dermatofibroma'
}

@csrf_exempt
def home(request):
    return HttpResponse("i am updating the views here")

@csrf_exempt
def predict(request):
    return HttpResponse("Hii i am image hamdler")