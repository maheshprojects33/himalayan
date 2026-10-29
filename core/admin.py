from django.contrib import admin
from core.models import *

# Admin For Home Page Models
class HeroImageSliderAdmin(admin.ModelAdmin):
    list_display = ('image_alt', 'image')

admin.site.register(HeroImageSlider, HeroImageSliderAdmin)

class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

admin.site.register(WhoWeAre, WhoWeAreAdmin)

class WhatWeMakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', )

admin.site.register(WhatWeMake, WhatWeMakeAdmin)

class OurCraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', )

admin.site.register(OurCraft, OurCraftAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', )

admin.site.register(Faq, FaqAdmin)

# Admin For About Page Models
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)

admin.site.register(AboutBanner, AboutBannerAdmin)

class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'note', 'description',)

admin.site.register(OurStory, OurStoryAdmin)

class MessageFromCEOAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'msg_higlight',)

admin.site.register(MessageFromCEO, MessageFromCEOAdmin)

class OurValueAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'title', 'description',)

admin.site.register(OurValue, OurValueAdmin)

class CapabilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'points',)

admin.site.register(Capability, CapabilityAdmin)

# Admin For Products Page Models
class FilterTagAdmin(admin.ModelAdmin):
    list_display = ('id','tag')

admin.site.register(FilterTag, FilterTagAdmin)

class AllProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'category')
    list_filter = ('category',)

admin.site.register(AllProducts, AllProductsAdmin)

class ProductOrderingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'title', 'description',)

admin.site.register(ProductOrdering, ProductOrderingAdmin)

# Admin For Our Craft Page Models
class OurCraftBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)

admin.site.register(OurCraftBanner, OurCraftBannerAdmin)

class OurCraftProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_image', 'note',)

admin.site.register(OurCraftProcess, OurCraftProcessAdmin)

class OurCraftQualityAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'title', 'description',)

admin.site.register(OurCraftQuality, OurCraftQualityAdmin)

class GalleryInsideAdmin(admin.ModelAdmin):
    list_display = ('image', 'title',)

admin.site.register(GalleryInside, GalleryInsideAdmin)

# Admin For Sustainability Page Models
class SustainabilityBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)

admin.site.register(SustainabilityBanner, SustainabilityBannerAdmin)

class SustainabilityCommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)

admin.site.register(SustainabilityCommunity, SustainabilityCommunityAdmin)

class SustainabilityPracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)

admin.site.register(SustainabilityPractice, SustainabilityPracticeAdmin)

class SustainabilityCommitmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)

admin.site.register(SustainabilityCommitment, SustainabilityCommitmentAdmin)
