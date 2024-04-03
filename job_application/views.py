from django.shortcuts import render
# Create your views here.
# we are creating a function to lead to the index.html file
def index(request):
    return render(request, "index.html")
