from django.contrib import admin
from .models import Review, Comment, Rating

admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Rating)
