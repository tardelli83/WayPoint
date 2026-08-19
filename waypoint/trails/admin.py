from django.contrib import admin
from .models import Trail, Park, TrailReport

admin.site.register(Trail)
admin.site.register(Park)
admin.site.register(TrailReport)