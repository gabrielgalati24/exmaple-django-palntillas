from django.shortcuts import render

# Create your views here.
#render home.html 
def home(request):
   return render(request, 'home.html')


# def home(request):
#     return render(request, 'home.html')