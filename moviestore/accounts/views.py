from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    template_data ={
        "title": "sign up",
    }
    # the logic for rendering the form page.
    if request.method == "GET":
        template_data = {
            'form' : UserCreationForm()
        }
        
        return render(request, 'accounts/signup.html',{'template_data':template_data})