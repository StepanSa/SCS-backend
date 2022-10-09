from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # creating fake users
        # registered_users = [('beb@gmail.com', 'bebbebbeb'),
        #                     ('bebbeb@gmail.com', 'beeeeeeb'),
        #                     ('bebebebey@gmail.com', 'bebebebey')]
        # for i in range(len(registered_users)):
        #     email1 = registered_users[i][0]
        #     password1 = registered_users[i][1]
        #     my_user = User.objects.create_user(username=email1.split("@")[0], email=email1, password=password1)
        #     my_user.is_active = True
        #     my_user.save()

        return HttpResponse({'beb'})


@csrf_exempt
def login_(request):
    registered_users = [('beb@gmail.com', 'bebbebbeb'),
                        ('bebbeb@gmail.com', 'beeeeeeb'),
                        ('bebebebey@gmail.com', 'bebebebey')]

    if request.method == 'GET':
        username = request.POST['email']
        password1 = request.POST['password']
        # username = username.split("@")[0]

        if (username, password1) not in registered_users:
            return HttpResponse("Wrong email or password")

        return redirect('index.html')

        # user = authenticate(username=username, password=password1)
        #
        # if user is not None:
        #     login(request, user)
        #     # messages.success(request, "Logged In Sucessfully!!")
        #     return redirect('index.html')
        # else:
        #     messages.error(request, "Bad Credentials!!")
        #     # return render(request, 'samepage.html')
        #     return HttpResponse({'badbadbadboy'})

    return render(request, 'samepage2.html')

