from django.db import models

from django.db import models

class HeroSection(models.Model):
    title_main = models.CharField(max_length=200, default="Unlock Your")
    title_gradient = models.CharField(max_length=200, default="Academic Potential")
    title_sub = models.CharField(max_length=200, default="with Proffyemphy's Ideal Academy")
    description = models.TextField(default="Access top-quality tutorials tailored for Nigerian university students. Learn at your own pace, anytime, anywhere with our comprehensive learning platform.")
    download_button_text = models.CharField(max_length=50, default="Download Now")
    download_button_link = models.URLField(blank=True, null=True)
    learn_more_button_text = models.CharField(max_length=50, default="Learn More")
    learn_more_button_link = models.URLField(blank=True, null=True)
    background_video = models.FileField(upload_to="hero_videos/", blank=True, null=True)

    def __str__(self):
        return self.title_main

class Statistic(models.Model):
    number = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} - {self.description}"




class AboutSection(models.Model):
    title_main = models.CharField(max_length=200, default="Empowering Nigerian Students")
    title_sub = models.CharField(max_length=200, default="to Excel Academically")
    description = models.TextField(default="Proffyemphy's Ideal Academy is dedicated to providing comprehensive tutorial support to students across all Nigerian universities. Our platform offers a wide range of courses, expert instructors, and interactive learning tools to help you excel in your studies.")

    def __str__(self):
        return self.title_main




class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    svg_icon = models.TextField(
        help_text="Paste the full SVG code here. Make sure to use double quotes for attributes."
    )
    color_from = models.CharField(max_length=7, default="#34D399")  # Tailwind green-400
    color_to = models.CharField(max_length=7, default="#10B981")    # Tailwind green-500

    def __str__(self):
        return self.title



class Aboutstat(models.Model):
    number = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} - {self.description}"




class Tutor(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tutors/')  # Upload photo via admin

    def __str__(self):
        return self.name




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    rating = models.PositiveSmallIntegerField(default=5)  # 1 to 5
    content = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.university}"






class VisionMission(models.Model):
    vision_title = models.CharField(max_length=100, default="Our Vision")
    vision_text = models.TextField(default="To become Nigeria’s leading online academic platform, equipping every student with the right knowledge, tools, and guidance to achieve excellence and compete globally.")
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_text = models.TextField(default="To provide accessible, affordable, and high-quality tutorial support that empowers Nigerian students to excel academically, fostering innovation, confidence, and lifelong learning.")

    def __str__(self):
        return "Vision & Mission"


class CTASection(models.Model):
    badge_text = models.CharField(max_length=100, default="Join the Success Story")
    heading_main = models.CharField(max_length=200, default="Ready to Get")
    heading_gradient = models.CharField(max_length=200, default="Started?")
    subtext = models.TextField(default="Join thousands of students who are achieving academic success with Proffyemphy's Ideal Academy. Sign up today and start your learning journey towards excellence.")
    button_text = models.CharField(max_length=100, default="Create Account Now")
    button_url = models.URLField(default="#")

    def __str__(self):
        return "CTA Section"

class CTAFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(help_text="Paste raw SVG code here")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


from django.db import models

class DownloadAppSection(models.Model):
    heading_main = models.CharField(max_length=100, default="Download the App")
    heading_highlight = models.CharField(max_length=100, default="Today")
    description = models.TextField(default="Access Proffyemphy's Ideal Academy on the go with our mobile app. Download now and start learning anytime, anywhere.")
    button_text = models.CharField(max_length=50, default="Download App")
    button_url = models.URLField(default="#")

    def __str__(self):
        return "Download App Section"


class DownloadAppFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    icon_svg = models.TextField(help_text="Paste raw SVG code here")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']




class Footer(models.Model):
    academy_name = models.CharField(max_length=255, default="Proffyemphy's Ideal Academy")
    description = models.TextField(default="Empowering Nigerian university students with comprehensive tutorial support and expert guidance for academic excellence.")
    
    email = models.EmailField(default="proffyemphy001@gmail.com")
    phone = models.CharField(max_length=50, default="+234 (0) 8128235805")
    address = models.TextField(default="5, Okeolokun street, Ok bustop, Agura-gberigbe, Ikorodu, Lagos state")

    logo = models.ImageField(upload_to="footer/", blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.academy_name
