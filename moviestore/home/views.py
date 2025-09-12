from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {
        'title': 'Movie Store'
    }
    return render(request,'home/index.html',{'template_data':template_data})

def about(request):
    template_data = {
        'title': 'About'
    }
    return render(request,'home/about.html',{'template':template_data})