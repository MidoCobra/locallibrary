from django.contrib.auth.models import User
import django_filters
from .models import Schools

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Schools
        fields = {
            'name':['icontains',]

        }
        verbose_name = "search school"