from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({"error": "Incorrect username or password"}, status=400)
        else:
            login(request, user)
            return JsonResponse({"success": "Login has been acepted"}, status=200)
    return redirect("/")


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]

            login(username=username, password=password)

            return JsonResponse(
                {"success": "You have successfully signed up"}, status=200
            )
        else:
            print(form.errors)
            return JsonResponse({"error": form.errors.as_text}, status=401)
    return redirect("/")


@login_required(login_url="page_not_found")
def logout_view(request):
    logout(request)
    return redirect("/")
