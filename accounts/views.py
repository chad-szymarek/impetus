from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


def signup(request):
    form = UserCreationForm(request.POST)
    form.help_texts = {'username': None, 'password1': None, 'password2': None}
    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            user.save()
            login(request, user)
            return redirect("home")

    context = {"form": form}
    return render(request, "registration/signup.html", context)
