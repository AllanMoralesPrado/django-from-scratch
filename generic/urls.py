from django.urls import path
from .views import GenericModelFormView
from .views import generic_form_view

urlpatterns = [
    #path('addgeneric/', GenericModelFormView.as_view(), name='addG')
    path('addgeneric/', generic_form_view, name='addG')
]
