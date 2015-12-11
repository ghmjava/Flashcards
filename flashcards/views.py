from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters

# Create your views here.

@login_required(login_url='/flashcards/login', redirect_field_name='index')
def index(request):
    user = request.user
    active = request.user.is_active
    return HttpResponse('index')
    
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponse('logged out')
    
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):

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
