
from django.urls import path
from . import views




urlpatterns = [
    path('' , views.homepage , name='homepage'),

    # path('logout/', views.logout_view, name='logout'),

     # READ
    path('influencers/', views.influencer_list, name='influencer_list'),
    path('influencer/<int:id>/profile/', views.profile_details, name='influencer_details'),
    path("influencer/profile/me/<int:id>/", views.my_profile, name="my_profile"),


    path('influencer/profile/create/', views.create_influencer, name='create_influencer'),  # C
    path('influencer/profile/edit/<int:id>/', views.update_influencer, name='profile_update'), # U
    path('influencer/profile/delete/<int:id>', views.delete_influencer, name='profile_delete') # D
    
]