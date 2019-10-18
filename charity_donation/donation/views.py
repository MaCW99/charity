from django.db.models import Sum, Count
from django.shortcuts import render

# Create your views here.
from django.views import View

from donation.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.aggregate(Sum('quantity'))
        count_inst = Donation.objects.values('institution').distinct().count()
        help_fundations = Institution.objects.filter(type=1)
        help_ngo = Institution.objects.filter(type=2)
        help_local = Institution.objects.filter(type=3)

        ctx = {
            'bags': bags,
            'help_fundations': help_fundations,
            'help_ngo': help_ngo,
            'help_local': help_local,
            'count_inst': count_inst

        }
        return render(request, 'index.html', ctx)


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterPage(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonationPage(View):
    def get(self, request):
        return render(request, 'form.html')
