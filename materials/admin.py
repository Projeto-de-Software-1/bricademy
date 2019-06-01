from django.contrib import admin
from .models import Material, Subject, Ad, Request, Complaint
# Register your models here.
admin.site.register(Material)
admin.site.register(Subject)
admin.site.register(Ad)
admin.site.register(Request)
admin.site.register(Complaint)
