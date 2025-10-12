from django.db import models

# Create your models here.

class InfluencerProfile(models.Model):
    influencer_id = models.BigAutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE) #related_name='influencer_profile'
    display_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=140 , unique=True)
    bio = models.TextField(blank=True)
    # avatar
    contact_email = models.EmailField(max_length=100,blank=False)
    country = models.CharField(max_length=15) #validators=True 
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.display_name

