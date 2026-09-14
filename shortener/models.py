from django.db import models
import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class URL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True, db_index=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            code = generate_short_code()
            while URL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            self.short_code = code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
