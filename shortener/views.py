from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect, render
from .models import URL
from .serializers import URLSerializer

def index(request):
    return render(request, 'shortener/index.html')

class ShortenURLView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectURLView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(URL, short_code=short_code)
        url_obj.clicks_count += 1
        url_obj.save()
        return redirect(url_obj.original_url)
