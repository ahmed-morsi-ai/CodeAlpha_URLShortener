from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'clicks_count', 'created_at']
        read_only_fields = ['short_code', 'clicks_count', 'created_at']

    def get_short_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/{obj.short_code}')
        return f'/{obj.short_code}'
