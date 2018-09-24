from django.urls import path

from . import views

app_name = "sortdrinks"
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]
