from django.contrib import admin
from .models import Gym, Member, Equipment

# Register your models here.
admin.site.register(Gym)
admin.site.register(Member)
admin.site.register(Equipment)