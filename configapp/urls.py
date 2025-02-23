from django.urls import path, include
from configapp.views import *

urlpatterns = [
    path('index/', index),
    path('carmodel/<int:carmodel_id>', carmodel_new, name='carmodel_new'),
    path('batch_all/<int:car_id>', batch_all , name='batch_all'),
    path('carmodels/', carmodels , name='carmodels'),
]
