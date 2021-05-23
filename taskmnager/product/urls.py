from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wed_1, name='wed_1'),
    path('sale_2/', views.sale_2, name='sale_2'),
    path('even_3/', views.even_3, name='even_3'),
    path('shoes_4/', views.shoes_4, name='shoes_4'),
    path('veil_5/', views.veil_5, name='veil_5'),
    path('access_6/', views.access_6, name='access_6'),

    path('<int:pk>', views.OwnPages1.as_view(), name='wedding'),
    path('sale_2/<int:pk>', views.OwnPages2.as_view(), name='sale'),
    path('even_3/<int:pk>', views.OwnPages3.as_view(), name='evening'),
    path('shoes_4/<int:pk>', views.OwnPages4.as_view(), name='shoes'),
    path('veil_5/<int:pk>', views.OwnPages5.as_view(), name='veil'),
    path('acess_6/<int:pk>', views.OwnPages6.as_view(), name='accessories'),

    path('filter/<int:pk>', views.type_filter, name='type_filter'),
    path('filter/veil_5/<int:pk>', views.type_filter5, name='type_filter5'),
    path('filter/access_6/<int:pk>', views.type_filter6, name='type_filter6'),
    path('filter/even_3/<int:pk>', views.type_filter3, name='type_filter3'),
    path('filter/wed_1/<int:pk>', views.type_filter1, name='type_filter1'),
]
