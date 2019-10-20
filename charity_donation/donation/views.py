from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from donation.models import Donation, Institution

from donation.forms import RegisterForm, LoginForm


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.aggregate(Sum("quantity"))
        count_inst = Donation.objects.values("institution").distinct().count()
        help_fundations = Institution.objects.filter(type=1)
        help_ngo = Institution.objects.filter(type=2)
        help_local = Institution.objects.filter(type=3)

        ctx = {
            "bags": bags,
            "help_fundations": help_fundations,
            "help_ngo": help_ngo,
            "help_local": help_local,
            "count_inst": count_inst,
        }
        return render(request, "index.html", ctx)


class LoginPage(View):
    def get(self, request):
        form = LoginForm()
        ctx = {"form": form}
        return render(request, "login.html", ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/register")
        else:
            form = LoginForm()
            ctx = {"form": form}
            return render(request, "login.html", ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterPage(View):
    def get(self, request):
        form = RegisterForm()
        ctx = {"form": form}
        return render(request, "register.html", ctx)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_2 = form.cleaned_data["password2"]

            if User.objects.filter(username=email).exists():
                ctx = {
                    "form": form,
                    "msg_bad": "Adres e-mail jest już zaresjestrowany!",
                }
                return render(request, "register.html", ctx)
            if password != password_2:
                ctx = {"form": form, "msg_bad": "Hasło musi być identyczne!"}
                return render(request, "register.html", ctx)

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            return HttpResponseRedirect("/login")
        else:
            ctx = {"form": form, "msg_bad": "Wypełnij formularz poprawnie!"}
            return render(request, "register.html", ctx)


class AddDonationPage(View):
    def get(self, request):
        return render(request, "form.html")
