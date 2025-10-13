from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class InfluencerProfile(models.Model):
    influencer_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='influencer_profile',
    null=True, blank=True      # ← temporary
    )
    display_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=140 , unique=True,blank=True) #it should be generated Automaticlly
    bio = models.TextField(blank=True)
    # avatar
    contact_email = models.EmailField(max_length=100,blank=False)
    country = models.CharField(max_length=15) #validators=True 
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.display_name

