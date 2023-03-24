import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name='date_published',
                                               lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='date_published',
                                             lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['start_date', 'end_date']