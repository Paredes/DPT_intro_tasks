from django.test import TestCase
from pytz import HOUR
from .models import Attendance
from django.utils import timezone
from datetime import timedelta,date,time

def create_actual_date(extra_days=None):
    now = timezone.now()
    if extra_days:
        now += timedelta(days=extra_days)
    return date(
        day=now.day,
        month=now.month,
        year=now.year
    )

class AttendanceModelTests(TestCase):

    def test_check_time_not_defined(self):
        now = timezone.now()
        attendance = Attendance(
            date=create_actual_date(),
        )
        self.assertIs(attendance.is_a_valid_period(), True)

    def test_attendance_in_future(self):
        future_attendance = Attendance(
            date=create_actual_date(extra_days=2),
        )
        self.assertIs(future_attendance.is_a_valid_date(), False)
        self.assertIs(future_attendance.is_a_valid_period(), True)

    def test_attendance_check_out_time_in_past(self):
        attendance = Attendance(
            date=create_actual_date(),
            check_in_time=time(hour=1,minute=0),
            check_out_time=time(hour=0,minute=0),
        )
        self.assertIs(attendance.is_a_valid_period(), False)
    
    def test_equal_check_time(self):
        time_example = time(hour=9,minute=0)
        attendance = Attendance(
            date=create_actual_date(),
            check_in_time=time_example,
            check_out_time=time_example,
        )
        self.assertIs(attendance.is_a_valid_period(), False)
    