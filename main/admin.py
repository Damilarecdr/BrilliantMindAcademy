from django.contrib import admin
from .models import HeroSection, Statistic, AboutSection, Tutor, Testimonial,   Feature,Aboutstat, Tutor, Testimonial,  VisionMission,  CTASection, CTAFeature, DownloadAppSection, DownloadAppFeature,  Footer

admin.site.register(HeroSection)
admin.site.register(Statistic)
admin.site.register(AboutSection)
admin.site.register(Aboutstat)
admin.site.register(Feature)

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualification', 'course')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'rating')


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('vision_title', 'mission_title')



@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('heading_main', 'heading_gradient')


@admin.register(CTAFeature)
class CTAFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


@admin.register(DownloadAppSection)
class DownloadAppSectionAdmin(admin.ModelAdmin):
    list_display = ('heading_main', 'heading_highlight')


@admin.register(DownloadAppFeature)
class DownloadAppFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("academy_name", "email", "phone", "updated_at")
