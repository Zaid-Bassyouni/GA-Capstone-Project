
from django.urls import path
from . import views




urlpatterns = [
    path('' , views.homepage , name='homepage'),

    path('influencer/profile/', views.profile_details, name='profile_details'),   # R
    path('influencer/profile/create/', views.profile_create, name='profile_create'),  # C
    path('influencer/profile/edit/', views.update_profile, name='profile_update'),  # U
    path('influencer/profile/delete/', views.delete_influencer, name='profile_delete') # D
]