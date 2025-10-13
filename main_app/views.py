from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import InfluencerProfileForm
from .models import InfluencerProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



def homepage(request):
      influencers = ['Jumana','Azeez','Zein','Omar']
      return render(request,'homepage.html',{ 'influencers':influencers})

# READ 
@login_required
def profile_details(request):
    profile = get_object_or_404(InfluencerProfile, user=request.user)
    return render(request, 'influencers/profile_details.html', { 'profile': profile })



# CREATE 
@login_required
def profile_create(request):
    if InfluencerProfile.objects.filter(user=request.user).exists():
        messages.info(request, "You already have a profile. You can edit it instead.")
        return redirect(reverse('profile_update'))

    if request.method == 'POST':
        form = InfluencerProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # attach to current user
            profile.save()
            messages.success(request, "Profile created successfully.")
            return redirect(reverse('profile_details'))
        messages.error(request, "Please fix the errors below.")
    else:  # GET
        form = InfluencerProfileForm()

    return render(request, 'influencers/profile_form.html', { 'form': form })


        
@login_required
def update_profile(request):
    # create one if missing (so page works the first time)
    profile, _ = InfluencerProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = InfluencerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect(reverse('profile_details'))
        messages.error(request, "Please fix the errors below.")
    else:  # GET
        form = InfluencerProfileForm(instance=profile)

    return render(request, 'influencers/profile_form.html', { 'form': form, 'profile': profile })


# DELETE
@login_required
def delete_influencer(request):
    profile = get_object_or_404(InfluencerProfile, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, "Profile deleted.")
        return redirect(reverse('homepage'))
    return render(request, 'influencers/profile_confirm_delete.html', { 'profile': profile })  