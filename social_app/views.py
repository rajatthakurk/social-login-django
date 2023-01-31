# from django.views.generic import TemplateView
# from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# class Home(TemplateView):
#     template_name = "dashboard.html"

# def dashboard(request):
#     if request.user.is_not_authenticated:
#         return render(request,'home.html')
#     else:
#         pass

def dashboard(request):
    return render(request,'dashboard.html')

def home(request):
    user = request.user
    # print(user)
    if user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'home.html')