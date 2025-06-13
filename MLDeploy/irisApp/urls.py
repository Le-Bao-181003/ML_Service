from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name='predictor'),  
    # path('result', view=views.predictor, name='result'),
]