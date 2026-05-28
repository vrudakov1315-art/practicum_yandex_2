from django.core.paginator import Paginator

from projects.constants import PAGINATE_BY


def paginate_queryset(queryset, page_number):
    paginator = Paginator(queryset, PAGINATE_BY)
    return paginator.get_page(page_number)
