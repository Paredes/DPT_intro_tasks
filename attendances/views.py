# -*- coding: utf-8 -*-
""" Views for the attendances application. """
# standard library

# django

# models
from .models import Attendance

# views
from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView

# forms
from .forms import AttendanceForm


class AttendanceListView(BaseListView):
    """
    View for displaying a list of attendances.
    """
    model = Attendance
    template_name = 'attendances/attendance_list.pug'
    permission_required = 'attendances.view_attendance'


class AttendanceCreateView(BaseCreateView):
    """
    A view for creating a single attendance
    """
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendances/attendance_create.pug'
    permission_required = 'attendances.add_attendance'


class AttendanceDetailView(BaseDetailView):
    """
    A view for displaying a single attendance
    """
    model = Attendance
    template_name = 'attendances/attendance_detail.pug'
    permission_required = 'attendances.view_attendance'


class AttendanceUpdateView(BaseUpdateView):
    """
    A view for editing a single attendance
    """
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendances/attendance_update.pug'
    permission_required = 'attendances.change_attendance'


class AttendanceDeleteView(BaseDeleteView):
    """
    A view for deleting a single attendance
    """
    model = Attendance
    permission_required = 'attendances.delete_attendance'
    template_name = 'attendances/attendance_delete.pug'
