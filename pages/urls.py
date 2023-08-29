from django.urls import path


from . import views


urlpatterns = [
    path("",views.HomePageView.as_view(),name='home'),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name='profile'),
    path('update/<int:pk>/',views.ProfileUpdateView.as_view(),name='profile_update'),


]
