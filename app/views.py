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



#def home(request):
#    menu_entries = MenuEntry.objects.all()
    
  
    
    return render(request, 'home.html', {'menu_entries': menu_entries})
