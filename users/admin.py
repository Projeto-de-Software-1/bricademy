from django.contrib import admin
from .models import Profile, Address, Evaluation

# Register your models here.
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Evaluation)
