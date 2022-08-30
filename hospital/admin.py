from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Doctor)
admin.site.register(Chief_Physician)
admin.site.register(Hospital)

