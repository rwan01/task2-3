from django.shortcuts import render, redirect
from .models import Login
from .forms import LoginForm


def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')



# def form(request):
#     Login(request.POST).save()

#     return render(request, "pages/form.html",{'Lf':LoginForm()})


def form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoginForm()

    return render(request, "pages/form.html", {"Lf": form})

# def form(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         Login.objects.create(username=username, password=password)

#     return render(request, "pages/form.html",{'Lf':LoginForm()})


