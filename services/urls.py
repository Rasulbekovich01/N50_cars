from django.urls import path

from services.views import home_page_view

urlpatterns = [
    path ('', home_page_view)
]