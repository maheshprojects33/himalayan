from unicodedata import category

from django.db import models

# Home Page Models
class HeroImageSlider(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    image_alt = models.CharField(max_length=64)
    
    def __str__(self):
        return self.image_alt

class WhoWeAre(models.Model):
    image = models.ImageField(upload_to='who_we_are_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    points = models.TextField(
        blank=True,
        help_text="Enter one bullet point per line.",
    )

    @property
    def points_list(self):
        return [line.strip() for line in self.points.splitlines() if line.strip()]

    def __str__(self):
        return self.title

class WhatWeMake(models.Model):
    image = models.ImageField(upload_to='what_we_make_images/')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title   

class OurCraft(models.Model):
    image = models.ImageField(upload_to='our_craft_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

# About Page Models
class AboutBanner(models.Model):
    image = models.ImageField(upload_to='about_header_images/')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

class OurStory(models.Model):
    image = models.ImageField(upload_to='our_story_images/')
    title = models.CharField(max_length=128)
    note = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Our Story"

    def __str__(self):
            return self.title

class MessageFromCEO(models.Model):
    image = models.ImageField(upload_to='ceo_images/')
    title = models.CharField(max_length=64)
    msg_higlight = models.CharField(max_length=255)
    message = models.TextField(max_length=1500)

    class Meta:
        verbose_name_plural = "Message From CEO"

    def __str__(self):
        return self.title

class OurValue(models.Model):
    s_no = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class Capability(models.Model):
    image = models.ImageField(upload_to='capability_images/')
    title = models.CharField(max_length=64)
    points = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Capability"

    @property
    def points_list(self):
        return [line.strip() for line in self.points.splitlines() if line.strip()]
    

    def __str__(self):
        return self.title

# Product Page Models
class FilterTag(models.Model):
    tag = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return self.tag

class AllProducts(models.Model):
    image = models.ImageField(upload_to='all_products/')
    
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(FilterTag, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class ProductOrdering(models.Model):
    s_no = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

# Our Craft Page Models
class OurCraftBanner(models.Model):
    image = models.ImageField(upload_to='our_craft_banner_images/')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

class OurCraftProcess(models.Model):
    craft = models.CharField(max_length=32)
    title_image = models.ImageField(upload_to='our_craft_handmade_paper/')
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=255)
    description = models.TextField()
    points = models.TextField()
    process_image_a = models.ImageField(upload_to='our_craft_handmade_paper/process_images_a/')
    a_title = models.CharField(max_length=32)
    a_process = models.TextField()
    process_image_b = models.ImageField(upload_to='our_craft_handmade_paper/process_images_b/')
    b_title = models.CharField(max_length=32)
    b_process = models.TextField()
    process_image_c = models.ImageField(upload_to='our_craft_handmade_paper/process_images_c/')
    c_title = models.CharField(max_length=32)
    c_process = models.TextField()
    

    @property
    def points_list(self):
        return [line.strip() for line in self.points.splitlines() if line.strip()]
    
    def __str__(self):
        return self.title

class OurCraftQuality(models.Model):
    s_no = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Our craft quality"

    def __str__(self):
        return self.title

class GalleryInside(models.Model):
    image = models.ImageField(upload_to='gallery_inside/')
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

# Sustainability Page Models
class SustainabilityBanner(models.Model):
    image = models.ImageField(upload_to='sustainability_banner_images/')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

class SustainabilityCommunity(models.Model):
    image = models.ImageField(upload_to='sustainability_community_images/')
    title = models.CharField(max_length=32)
    description = models.TextField()
    points = models.TextField()

    class Meta:
        verbose_name_plural = "Sustainability community"
    
    @property
    def points_list(self):
        return [line.strip() for line in self.points.splitlines() if line.strip()]

    def __str__(self):
        return self.title

class SustainabilityPractice(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class SustainabilityCommitment(models.Model):
    image = models.ImageField(upload_to='sustainability_commitment_images/')
    title = models.CharField(max_length=128)
    note = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.title