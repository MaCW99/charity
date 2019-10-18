from django.shortcuts import render

# Create your views here.
from django.views import View


class LandingPage(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterPage(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonationPage(View):
    def get(self, request):
        return render(request, 'form.html')
