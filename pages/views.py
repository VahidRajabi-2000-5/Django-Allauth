from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy


from accounts.forms import CustomUserChangeFormWithoutPassword


class HomePageView(generic.TemplateView):
    template_name ='pages/home.html'
    


class ProfileView(generic.DeleteView):
    model = get_user_model()
    template_name = 'pages/profile.html'  
    context_object_name = 'pro'
    

        
class ProfileUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeFormWithoutPassword
    template_name = 'pages/profile_update.html'
    context_object_name ='form'
    
    