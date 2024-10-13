from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from .models import MenuEntry


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após login bem-sucedido
        else:
            messages.error(request, 'Login inválido. Por favor, tente novamente.')
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .models.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Definir a senha corretamente
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirecione para a página de login ou outra página
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')