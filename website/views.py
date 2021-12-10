from collections import namedtuple
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from . import models
from . import forms
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def index(request):
    contact = models.Contact.objects.all()
    form = forms.ContactForm()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['bbchanna@gmail.com'])

        # send_mail('Contact Form',
        #           data,
        #           settings.EMAIL_HOST_USER,
        #           ['bbchanna@gmail.com'],
        #           fail_silently=False,
        #           )

        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'index.html', context)
