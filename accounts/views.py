from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignupView(CreateView):
    '''create view for signup'''
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '../templates/registration/signup.html'
    