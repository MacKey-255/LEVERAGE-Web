from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.is_staff:
        return redirect('home')

    return render(request, "index.html")
