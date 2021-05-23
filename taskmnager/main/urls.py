from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index),
    path('wedding-dresses', views.wedding),
    path('sale', views.sale),
    path('evening-dresses', views.evening),
    path('shoes', views.shoes),
    path('veil', views.veil),
    path('accessories', views.accessories),
    path('contacts', views.contacts),
    path('about', views.about),
    path('delivery', views.delivery),
    path('refund', views.refund),
    path('bank', views.bank),
    path('ourBride1', views.ourBride1),
    path('ourBride2', views.ourBride2),
    path('ourBride3', views.ourBride3),
    path('ourBride4', views.ourBride4),
    path('ourBride5', views.ourBride5),
    path('ourBride6', views.ourBride6),
    path('ourBride7', views.ourBride7),
    path('ourBride8', views.ourBride8),
    path('create', views.create),
    path('search', views.search),
]
