from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AttendancesConfig(AppConfig):
    name = 'attendances'
    verbose_name = _('attendances')
