from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.AttendanceListView.as_view(),
        name='attendance_list'
    ),
    path(
        'create/',
        views.AttendanceCreateView.as_view(),
        name='attendance_create'
    ),
    path(
        '<int:pk>/',
        views.AttendanceDetailView.as_view(),
        name='attendance_detail'
    ),
    path(
        '<int:pk>/update/',
        views.AttendanceUpdateView.as_view(),
        name='attendance_update'
    ),
    path(
        '<int:pk>/delete/',
        views.AttendanceDeleteView.as_view(),
        name='attendance_delete',
    ),
]
