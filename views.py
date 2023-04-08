from django.shortcuts import render
from django.http import HttpResponse

def view_login_page(request):
    return render(request, 'login_screen.html')

def verify(request):
    return HttpResponse('SAME SCREEN OR HOME SCREEN')

def signup_screen1(request):
    return render(request, 'signup_screen1.html')

def signup_screen2(request):
    return render(request, 'signup_screen2.html')

def signup_screen3(request):
    return render(request, 'signup_screen3.html')

def signup_screen4(request):
    return render(request, 'signup_screen4.html')

def forgot_screen1(request):
    return render(request, 'forgot_screen1.html')

def forgot_screen2(request):
    return render(request, 'forgot_screen2.html')