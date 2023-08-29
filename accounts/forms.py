from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'age', 'first_name', ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username','first_name', 'last_name', 'age', ]
    
    
class CustomUserChangeFormWithoutPassword(CustomUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'age']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']
        
        
""" class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(CustomUserCreationForm.base_fields)
        self.fields['email'].required = True
        
    def save(self, request):
        user = super().save(request)
        user.age = self.cleaned_data['age']
        user.save()
        return user """