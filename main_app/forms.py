from django import forms
from django.utils.text import slugify
from .models import InfluencerProfile

class InfluencerForm(forms.ModelForm):
    class Meta:
        model = InfluencerProfile
        fields = ["display_name", "bio", "contact_email", "country", "is_public", "is_active",
                  'instagram_url', 'tiktok_url', 'youtube_url', 'twitter_url', 'facebook_url',
                  ]

    def save(self, commit=True):
        obj = super().save(commit=False)
        from django.utils.text import slugify
        base = slugify(obj.display_name) or 'user'
        slug, i = base, 2
        qs = InfluencerProfile.objects.exclude(pk=obj.pk) if obj.pk else InfluencerProfile.objects.all()
        while qs.filter(slug=slug).exists():
            slug = f"{base}-{i}"; i += 1
        obj.slug = slug
        if commit: obj.save()
        return obj
