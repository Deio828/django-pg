from django.contrib import admin
from .models import Profile

# This step is made to add this model to the admin pannel page
admin.site.register(Profile)
