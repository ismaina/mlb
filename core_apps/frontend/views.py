from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def contact(request):

    context = {}

    return render(request, 'contact/contactform.html', context)