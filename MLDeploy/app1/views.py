from django.http import HttpResponse
from django.shortcuts import render

def Welcome(request):
    return render(request, 'index.html')

def User(request):
    username = request.GET['username']
    print(f"Username: {username}")  # Debugging output
    return render(request, 'user.html', {'name': username})