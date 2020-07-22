"""Posts URLs."""

# Django
from django.urls import path

# Views
from sites import views

urlpatterns = [

    path(
        route='',
        view=views.list_sites,
        name='feed'
    )
]
