from django.shortcuts import render



from django.shortcuts import render

from .models import HeroSection, Statistic, AboutSection, Feature, Aboutstat, Tutor,  Testimonial,VisionMission, CTASection, CTAFeature, DownloadAppSection, DownloadAppFeature,  Footer

def home(request):
    hero = HeroSection.objects.first()   
    stats = Statistic.objects.all()      
    about = AboutSection.objects.first() 
    features = Feature.objects.all()
    abt = Aboutstat.objects.all()   
    tutors = Tutor.objects.all()   
    testimonials = Testimonial.objects.all()
    vision_mission = VisionMission.objects.first()
    cta_section = CTASection.objects.first()  
    cta_features = CTAFeature.objects.all()
    download_app = DownloadAppSection.objects.first()  
    download_features = DownloadAppFeature.objects.all()

    context = {
        "hero": hero,
        "stats": stats,
        "about": about,
        "abt": abt,
        "features": features,
        "tutors": tutors,
        "testimonials": testimonials, 
        "vision_mission": vision_mission,
        "cta_section": cta_section,
        "cta_features": cta_features,
        "download_app": download_app,
        "download_features": download_features,
       
    }
    return render(request, "main/home.html", context)




from django.shortcuts import render
from .models import Footer

def footer_view(request):
    footer = Footer.objects.first()  # get the first footer record
    return render(request, "footer.html", {"footer": footer})


