from django.contrib import admin
from .models import Question

# we need to tell the admin that Question objects have an admin interface. 

admin.site.register(Question)