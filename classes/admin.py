from django.contrib import admin
from .models import *

# register all models in the admin
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Seance)
admin.site.register(Absent)
