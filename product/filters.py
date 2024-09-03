import django_filters

from product.models import Product


class ProductsFilter(django_filters.FilterSet):
        name = django_filters.CharFilter(lookup_expr='iexact')
        keyword = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
        min_price = django_filters.NumberFilter(field_name="price" or 0, lookup_expr="gte")
        max_price = django_filters.NumberFilter(field_name="price" or 0, lookup_expr="lte")
        class Meta:
            model = Product
            fields = ('category','keyword','min_price','max_price')