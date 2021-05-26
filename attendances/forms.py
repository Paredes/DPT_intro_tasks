# -*- coding: utf-8 -*-
""" Forms for the attendances application. """
# standard library

# django
from django import forms

# models
from .models import Attendance

# views
from base.forms import BaseModelForm


class AttendanceForm(BaseModelForm):
    """
    Form Attendance model.
    """

    class Meta:
        model = Attendance
        exclude = ()
