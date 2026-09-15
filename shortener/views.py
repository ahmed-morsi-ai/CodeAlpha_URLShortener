from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortenedURL
from .serializers import ShortenURLSerializer

class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortenURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectURLView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedURL, short_code=short_code)
        ShortenedURL.objects.filter(pk=url_obj.pk).update(clicks=F('clicks') + 1)
        return redirect(url_obj.original_url)

class URLAnalyticsView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedURL, short_code=short_code)
        serializer = ShortenURLSerializer(url_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

def index_view(request):
    return render(request, 'shortener/index.html')
