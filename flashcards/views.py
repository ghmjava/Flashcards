from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from mobica import settings
import json
from django.core import serializers

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponse('logged out')

def test(request):
    
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return HttpResponse("test")

@sensitive_post_parameters()
@csrf_protect
@never_cache
def logged(request):

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if not username or not password:
        return render(request, 'flashcards/login.html')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("logged")
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            return HttpResponse("inactive")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("invalid")

def start_quiz(request):
    
    dictionary = request.GET.get('dictionary', None)
    questions = request.GET.get('questions', None)

    return render(request, 'quiz.html', {"dictionary": dictionary, "questions":questions})
