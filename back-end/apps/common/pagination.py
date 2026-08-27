from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """Standard `?page=` pagination with an opt-in `?page_size=`, capped so a
    client can't accidentally (or deliberately) ask for the whole table."""

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100
