from rest_framework.pagination import PageNumberPagination


class ResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page = 1
    page_size = 10
    max_page_size = 100
