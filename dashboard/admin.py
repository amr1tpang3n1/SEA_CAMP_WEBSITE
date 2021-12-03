from django.contrib import admin
from dashboard.models import *

# Register your models here.
admin.site.site_header = "SEA Bootcamp Admin Panel"
admin.site.register(webInterfaceData)

