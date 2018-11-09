# authenticate module verifies that a given user details exit in the database
# login module attaches a session id
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginForm

from django.views.generic import View

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout


class Login(auth_views.LoginView):
    template_name = 'core/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm()

        # Get login form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # Create user session
                login(request, user)
                return redirect("/home/")
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/login/")

def home(request):
    return render(request, 'core/home.html')
