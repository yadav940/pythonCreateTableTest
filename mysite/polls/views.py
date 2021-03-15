from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# Create your views here.
from .models import Student
from .serializer import SudentSerializer


def index(request):
    return HttpResponse("Hello world")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def student_detail(request):
    std = Student.objects.get(id = 1)
    print(std)
    serializer = SudentSerializer(std)


    return Response(serializer.data)