from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User


def login_(request):
    # creating fake users
    registered_users = {'beb@gmail.com': 'bebbebbeb',
                         'bebbeb@gmail.com': 'beeeeeeb',
                         'bebebebey@gmail.com': 'bebebebey'}
    for (email, password) in registered_users:
        my_user = User.objects.create_user(username=email, email=email, password=password)
        my_user.is_active = False
        my_user.save()

    if request.method == 'POST':
        username = request.POST['email']
        password1 = request.POST['password']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect('index.html')
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, 'samepage.html')

    return render(request, 'samepage.html')

