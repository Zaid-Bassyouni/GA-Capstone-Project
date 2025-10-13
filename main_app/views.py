from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import InfluencerForm
from .models import InfluencerProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    # model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')   

    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, "Account created! Please log in.")
        return resp


def logout_view(request):
   LogoutView(request)  # This clears the user’s session
   return redirect('login')  # redirect to your login page name
    

# **************************************************************************



def homepage(request):
    influencers = InfluencerProfile.objects.all()
    return render(request, 'homepage.html', {'influencers': influencers})

def profile_details(request, id):
    profile = get_object_or_404(InfluencerProfile, influencer_id=id)
    return render(request, 'influencers/influencer_details.html', {'profile': profile})

def influencer_list(request):
    profiles = InfluencerProfile.objects.all()
    return render(request, 'influencers/all-influencers.html', {'profiles': profiles})


def create_influencer(request):
    if request.method == 'POST':
        form = InfluencerForm(request.POST)
        if form.is_valid():
            profile = form.save()          # no user linking
            return redirect('influencer_details', id=profile.influencer_id)
    else:
        form = InfluencerForm()
    return render(request, 'influencers/influencer_form.html', {'form': form})

def update_influencer(request, id):
    influencer = get_object_or_404(InfluencerProfile, influencer_id=id)
    if request.method == 'POST':
        form = InfluencerForm(request.POST, instance=influencer)
        if form.is_valid():
            form.save()
            return redirect('influencer_details', id=influencer.influencer_id)
    else:
        form = InfluencerForm(instance=influencer)
    return render(request, 'influencers/influencer_form.html', {'form': form})

def delete_influencer(request, id):
    profile = get_object_or_404(InfluencerProfile, influencer_id=id)
    if request.method == 'POST':
        profile.delete()
        return redirect('influencer_list')
    return render(request, 'influencers/profile_confirm_delete.html', {'profile': profile})




# READ 
# @login_required
# def profile_details(request):
#     profile = InfluencerProfile.objects.filter(user = request.user).filter()
#     if not profile:
#         messages.info(request,'Create your profile to get started!')
#         return redirect('create_influencer')
#     return render(request, 'influencers/influencer_details.html', { 'profile': profile })

# def profile_details(request,id):
#     influencer_profile = InfluencerProfile.objects.get(influencer_id = id)
#     return render(request,'influencers/influencer_details.html',{'influencer_profile':influencer_profile})


# # CREATE 
# # @login_required
# def create_influencer(request):
#     if InfluencerProfile.objects.filter(user=request.user).exists():
#         messages.info(request, "You already have a profile. You can edit it instead.")
#         return redirect(reverse('profile_update'))

#     if request.method == 'POST':
#         form = InfluencerForm(request.POST)
#         if form.is_valid():  # validate the inputs from the user
#             # profile = form.save(commit=False)
#             profile = form.save()
#             profile.user = request.user  # attach to current user
#             profile.save()
#             # messages.success(request, "Profile created successfully.")
#             return redirect(reverse('influencer_list') ) # from reverse('profile_details') -> reverse('influencer_list') which takes you into READ
#         # messages.error(request, "Please fix the errors below.")
#         else:
#             return render(request, 'influencers/influencer_form.html', { 'form': form })
#     elif request.method == 'GET':  # GET
#         form = InfluencerForm()
#         return render(request, 'influencers/influencer_form.html', { 'form': form }) #from 'influencers/profile_form.html' into influencers/influencer_form.html
#                                                         # it sends an instance of the form here

        
# @login_required
# def update_profile(request):
#     # require existing profile
#     try:
#         profile = request.user.influencer_profile
#     except InfluencerProfile.DoesNotExist:
#         messages.info(request, "Please create your profile first.")
#         return redirect('create_influencer')

#     if request.method == 'POST':
#         form = InfluencerForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated.")
#             return redirect('profile_details')
#     else:
#         form = InfluencerForm(instance=profile)

#     return render(request, 'influencers/influencer_form.html', #from 'influencers/profile_form.html' into influencers/influencer_form.html
#                   {'form': form, 'profile': profile})

# def update_influencer(request,id):
#     influencer = InfluencerProfile.objects.get(pk = id)

#     if request.method == 'POST':
#         form = InfluencerForm(request.POST, instance=influencer)
#         if form.is_valid():
#             influencer = form.save()
#             # return redirect(f'/influencers/{influencer.influencer_id}')
#             return redirect('influencer_details', id=influencer.influencer_id)
#         else:
#             return render(request, 'influencers/influencer_form.html',{'form':form})        
#     elif request.method == 'GET':

#         form = InfluencerForm(instance=influencer) #fills my form with the author that was fetched from the db
#         return render(request, 'influencers/influencer_form.html',{'form':form})

# # DELETE
# # @login_required
# def delete_influencer(request):
#     profile = InfluencerProfile.objects.filter(user=request.user).first()
#     if not profile:
#         messages.info(request, "You don't have a profile yet.")
#         return redirect('create_influencer')

#     if request.method == 'POST':
#         profile.delete()
#         messages.success(request, "Profile deleted.")
#         return redirect('homepage')

#     return render(request, 'influencers/profile_confirm_delete.html', {'profile': profile})

# ###################################################################################
# This is BrainStorming 

# CRUD :

#  1. we first create homepage to render the homepage.html file 

#  2. READ: define a function (e.g. def author-list(request): )->
#  - gets all authors from my database (using the model Auth for exampl)
#  - renders 'all-authors.html' file 

#  3. CREATE: the most hard to understand because we need to create form first:
#  1. in your forms.py you must create the following:
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['first_name','is_best_seller']
#         error_messages = {
#             "first_name": {
#                 "max_length": "Keep it short, please."
#             }
#         }
# NOTICE: your fields should be matching with your model required fields.
# NOTICE: In the CREATION the first part is always (get) -> if you see a page then it's (get-request)
#  so in the creation part we first check is the method is post or get
#  2. You have to pass your form into your author-form.html page.