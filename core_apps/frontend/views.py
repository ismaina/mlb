from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        print(request.POST, '\n\n\n\n\n\n\n\n')
        if form.is_valid():
            form.save()
            context['form'] = form
            context['success'] = form.instance
            return render(request, 'contact/contactform.html', context)
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
    context['form'] = form
    return render(request, 'contact/contactform.html', context)

def about(request):
    context = {}
    return render(request, 'contact/aboutus.html', context)