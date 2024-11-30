from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def tarifs(request):
    return render(request, 'website/tarifs.html')

def fonctionnalites(request):
    return render(request, 'website/fonctionnalites.html')

def essai_gratuit(request):
    return render(request, 'website/essai-gratuit.html')

def contact(request):
    return render(request, 'website/contact.html')

def blog(request):
    return render(request, 'website/blog.html')

def assistance(request):
    return render(request, 'website/assistance.html')

def a_propos(request):
    return render(request, 'website/a-propos.html')

