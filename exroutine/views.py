from django.shortcuts import redirect, render
from django.contrib.auth import logout
from exassemble.forms import UserForm
from django.contrib.auth import models, authenticate, login


def customLogout(request):
    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                email = data['email']
                password = data['password']
                user_permissions = data['user_permissions']
                user = models.User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user.user_permissions.set(user_permissions)
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.is_staff = data['is_staff']
                user.is_active = data['is_active']
                user.is_superuser = data['is_superuser']
                user.last_login = data['last_login']
                user.date_joined = data['date_joined']
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('index')
        else:
            form = UserForm()
            return render(request, 'register.html', {'form': form})
    return redirect('index')
