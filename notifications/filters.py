from django_filters import rest_framework as filters
from .models import Notification

class NotificationFilter(filters.FilterSet):
    is_attended = filters.BooleanFilter(field_name='is_attended')
    area = filters.CharFilter(field_name='area', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    attended_by = filters.CharFilter(field_name='attended_by__username', lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    attended_at = filters.DateFromToRangeFilter(field_name='attended_at')

    class Meta:
        model = Notification
        fields = ['is_attended', 'area', 'name', 'attended_by', 'created_at', 'attended_at']