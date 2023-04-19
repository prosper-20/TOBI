from django.urls import path
from .views import product_page, about_page

urlpatterns = [
    path("", product_page),
    path("about/", about_page, name="about-anything")
]
