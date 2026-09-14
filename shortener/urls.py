from django.urls import path
from .views import ShortenURLView, RedirectURLView, index

urlpatterns = [
    path('', index, name='home'),
    path('api/shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>', RedirectURLView.as_view(), name='redirect-url'),
]
