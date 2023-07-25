from django.shortcuts import render, get_object_or_404, redirect
from .models import User

# Create your views here.
def home(request):
    usuarios = User.objects.all()
    return render(request, 'home/index.html', {'usuarios': usuarios})


def create_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')
        User.objects.create(nome=nome, cidade=cidade)
        usuarios = User.objects.all()
    return render(request, 'home/index.html', {'usuarios': usuarios})


def edit_user(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.cidade = request.POST.get('cidade')
        usuario.save()
        return redirect('home')
    return render(request, 'home/update.html', {'usuario': usuario})


def delete_user(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    return redirect('home')