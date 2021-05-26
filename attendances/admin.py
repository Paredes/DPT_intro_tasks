# -*- coding: utf-8 -*-
""" Administration classes for the attendances application. """
# standard library

# django
from django.contrib import admin

# models
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass
