from django.urls import path

from website.views import index,blog,tarifs,fonctionnalites,essai_gratuit,assistance,a_propos,contact

urlpatterns = [
    path('',index,name='index'),
    path('tarifs/',tarifs,name='tarifs'),
    path('blog/',blog,name='blog'),
    path('fonctionnalites',fonctionnalites,name='fonctionnalites'),
    path('essai-gratuit/',essai_gratuit,name='essai-gratuit'),
    path('assistance/',assistance,name='assistance'),
    path('a-propos/',a_propos,name='a-propos'),
    path('contact/',contact,name='contact'),
]