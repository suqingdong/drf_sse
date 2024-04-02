from django.urls import path, include

from .views import MyView


urlpatterns = [
    path('', MyView.as_view(), name='myview'),
]