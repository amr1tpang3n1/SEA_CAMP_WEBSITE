from django.db import models


# Create your models here.
class webInterfaceData(models.Model):
    title_sc = models.CharField(max_length=100)
    title_1st = models.CharField(max_length=100)
    title_2nd = models.CharField(max_length=100)
    title_3rd = models.CharField(max_length=100)
    title_4th = models.CharField(max_length=100)
    event_venue_date = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    about_event = models.CharField(max_length=300)
    where_event = models.CharField(max_length=300)
    when_event_day = models.CharField(max_length=100)
    when_event_date = models.CharField(max_length=100)
    event_logo = models.ImageField(upload_to ='uploads/')
    venue = models.CharField(max_length=200)
    venue_about = models.CharField(max_length=400)
    background_top = models.ImageField(upload_to='uploads/')





