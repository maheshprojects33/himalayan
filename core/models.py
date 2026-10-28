from django.db import models

# Create your models here.
class HeroImageSlider(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    image_alt = models.CharField(max_length=50)
    
    def __str__(self):
        return self.image_alt

class WhoWeAre(models.Model):
    image = models.ImageField(upload_to='who_we_are_images/')
    image_alt = models.CharField(max_length=50)
    
    def __str__(self):
        return self.image_alt

class WhatWeMake(models.Model):
    image = models.ImageField(upload_to='what_we_make_images/')
    image_alt = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title   

class AboutBanner(models.Model):
    image = models.ImageField(upload_to='about_header_images/')
    image_alt = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

class MessageFromCEO(models.Model):
    image = models.ImageField(upload_to='ceo_images/')
    image_alt = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    msg_higlight = models.CharField(max_length=255)
    message = models.TextField(max_length=1500)