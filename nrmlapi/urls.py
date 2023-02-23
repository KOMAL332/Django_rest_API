from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('post-details/', post_details),
    path('get-details/', get_details)
]
