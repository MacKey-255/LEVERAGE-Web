from django.shortcuts import render, redirect


def home(request):
    if request.user.is_anonymous:
        return redirect('login')

    return render(request, "index.html")
