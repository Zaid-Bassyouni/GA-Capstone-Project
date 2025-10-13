from django import forms
from django.utils.text import slugify
from .models import InfluencerProfile

class InfluencerProfileForm(forms.ModelForm):
    class Meta:
        model = InfluencerProfile
        fields = ["display_name" , "bio","contact_email" , "country" , "is_public" , "is_active" ]

    def save(self, commit=True):
        obj = super().save(commit=False)
        if not obj.slug and obj.display_name:
            obj.slug = slugify(obj.display_name)
        if commit:
            obj.save()
        return obj