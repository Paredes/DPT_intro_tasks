# -*- coding: utf-8 -*-
""" Models for the attendances application. """
# standard library

# django
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# models
from base.models import BaseModel
from users.models import User
from .managers import AttendanceQuerySet
from datetime import date, time

class Attendance(BaseModel):
    """
    TODO: Fill this description
    The attendances system is used to store attendance.
    """
    # foreign keys
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )
    # required fields
    date = models.DateField(
        _('Date'),
        default=date.today,
    )
    check_in_time = models.TimeField(
        _('check in time'),
        default=time(hour=9,minute=0),
    )
    check_out_time = models.TimeField(
        _('check out time'),
        default=time(hour=18,minute=0),
    )
    # optional fields

    # Manager
    objects = AttendanceQuerySet.as_manager()

    class Meta:
        verbose_name = _('attendance')
        verbose_name_plural = _('attendances')

    def __str__(self):
        day_formatted = self.date.strftime("%d/%m/%Y")
        time_format = lambda t: t.strftime('%H%M')
        return f'{day_formatted} ({time_format(self.check_in_time)}-{time_format(self.check_out_time)})'
    
    def is_a_valid_period(self):
        return self.check_in_time < self.check_out_time

    def is_a_valid_date(self):
        now = timezone.now()
        return self.date <= date(day=now.day,month=now.month,year=now.year)

    def get_absolute_url(self):
        """ Returns the canonical URL for the Attendance object """
        # TODO this is an example, change it
        return reverse('attendance_detail', args=(self.pk,))
