from django.contrib import admin
from core.models import *

# Register your models here.
class HeroImageSliderAdmin(admin.ModelAdmin):
    list_display = ('image_alt', 'image')

admin.site.register(HeroImageSlider, HeroImageSliderAdmin)

class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = ('image_alt', 'image')

admin.site.register(WhoWeAre, WhoWeAreAdmin)

class WhatWeMakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'image_alt')

admin.site.register(WhatWeMake, WhatWeMakeAdmin)

class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'image_alt')

admin.site.register(AboutBanner, AboutBannerAdmin)

class MessageFromCEOAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'msg_higlight', 'image_alt')

admin.site.register(MessageFromCEO, MessageFromCEOAdmin)