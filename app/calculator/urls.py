from django.urls import path

from .views import CalculatorView

urlpatterns = [
    path('add_one/', CalculatorView.as_view({"post": "add_one_to_number"}))
]
