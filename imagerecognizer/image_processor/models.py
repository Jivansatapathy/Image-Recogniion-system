from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    

class CropRecommendation(models.Model):
    nitrogen = models.IntegerField()
    patassium = models.IntegerField()
    calcium = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    result = models.TextField()


class FertilizerRecommendation(models.Model):
    nitrogen = models.IntegerField()
    patassium = models.IntegerField()
    calcium = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture =  models.IntegerField()
    soil = models.TextField()
    croptype = models.TextField()
    result = models.TextField()