from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    if (request.user.is_authenticated):
        context = { 'username' : request.user.username }
        return render(request, "client/gameRoom.html", context)
    else:
        return redirect('/login', permanent=True)

def sign_up(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/', permanent=True)
    else:
        form = UserCreationForm()
    return render(request, 'client/signup.html', { 'form': form })

def login_request(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', permanent=True)
    return render(request, 'client/login.html')

def logout_request(request):
    logout(request)
    return redirect('/', permanent=True)