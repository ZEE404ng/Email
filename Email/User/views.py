from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail('subject', 'message', settings.EMAIL_HOST_USER, [address])
                context['User'] = 'Email sent successfully'
            except Exception as e:
                context['User'] = f'Error sending email: {e}'
        else:
            context['User'] = 'All fields are required'
    
    return render(request, "index.html", context)

def login_view(request):
    my_context = { 
        "my_text": "TEXT FOR TESTING"
    }
    return render(request, "login.html", my_context) 

