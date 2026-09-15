from django.urls import path
from .views import ShortenURLView, RedirectURLView, URLAnalyticsView, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('api/shorten/', ShortenURLView.as_view(), name='api-shorten'),
    path('api/analytics/<str:short_code>/', URLAnalyticsView.as_view(), name='api-analytics'),
    path('<str:short_code>/', RedirectURLView.as_view(), name='redirect'),
]
