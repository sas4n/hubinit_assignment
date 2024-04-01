from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:pk>/', views.BlogDetail.as_view()),
]

#this will make us choose our desired format, for instance, if the url ends with .json the receiving data would be in json format.
urlpatterns = format_suffix_patterns(urlpatterns)