from django.urls import path
from .import api
urlpatterns = [
    path('',api.SchoolApiListView.as_view()),
    path('<int:pk>',api.SchoolAPIDetails.as_view())
]
