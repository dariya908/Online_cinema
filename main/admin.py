from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Category,Genre,Movie,Rating, Comment])