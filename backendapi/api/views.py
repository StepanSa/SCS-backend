from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm


def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")


@csrf_exempt
def register(request):
    # GET we disply the form
    # POST we save the data

    context = {}

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # flash message

            user = form.save()
            messages.success(
                request,
                f"$! You are now able to log in",
            )

            return redirect("login")

    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)


@csrf_exempt
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return HttpResponse({'GGWP'})
        else:
            # messages.error(request, "Bad Credentials!!")
            return HttpResponse({'badbadbadboy'})
