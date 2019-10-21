"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from donation.views import (
    LandingPage,
    LoginPage,
    RegisterPage,
    AddDonationPage,
    LogoutView,
    UserDetailsPage,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^$", LandingPage.as_view(), name="landing_page"),
    url(r"^login/$", LoginPage.as_view(), name="login"),
    url(r"^register/$", RegisterPage.as_view(), name="register"),
    url(r"^add_donation/$", AddDonationPage.as_view(), name="add_donation"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),
    url(r"^user_site/$",UserDetailsPage.as_view(), name = "user_details"),

]
