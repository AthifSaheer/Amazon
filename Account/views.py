from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = UserRegistrationForm
    success_url = '/'

    def form_valid(slef, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = User.objects.create(username=username, email=email, password=password)
        user.save(commit=save)
        return super().form_valid(form)