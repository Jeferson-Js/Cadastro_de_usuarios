from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Home'
    return render(request, 'home/index.html', {'title': title})