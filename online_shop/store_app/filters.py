from django_filters.rest_framework import FilterSet
from .models import Todo



class TodoFilterSet(FilterSet):
    class Meta:
        model = Todo
        fields = {
            'completed':['exact'],
            'created_date':['gt', 'lt']
        }
