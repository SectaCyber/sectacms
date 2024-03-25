from django.urls import path
from sectacms.views import search

urlpatterns = [
    path("", search, name="Secta_search"),
]
