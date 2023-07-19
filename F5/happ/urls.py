from django.urls import path
from happ import views

urlpatterns = [
    path('abc/',views.result_view),
]