from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
# we are creating a function to lead to the index.html file

# here, we are are going to capture the values of the job application form
# they will be placed in the django database


# This what we change our code too. 
# cleaned_data is a function from the forms module that makes sure that the data is 
# a dictionary and has a value to it

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)

            Form.objects.create(first_name=first_name, last_name=last_name,email=email, 
                                date=date, occupation=occupation)
            
            # message email goes here
            message_body = f"A new job application was submitted. Thank you, {first_name}."
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")


