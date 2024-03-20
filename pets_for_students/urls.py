from django.urls import path
from pets_for_students import views

app_name = 'pets_for_students'

urlpatterns = [
path('', views.index, name='index'),
path('cats/', views.cats, name='cats')
]