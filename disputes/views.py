from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect

from contacts.models import Contacts

from .forms import ContactForm

def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message= form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            query = Contacts(name = name, phone = phone, subject = subject, message = message, from_email = from_email)
            query.save()
        try:
            send_mail(subject, message, from_email, ['jai@venkat.co.uk'])
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('success')

    return render(request, "index.html", {'form': form})

def success(request):
    return HttpResponse('Success, Thanks')

