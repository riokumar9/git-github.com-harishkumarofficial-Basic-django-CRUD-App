from rest_framework.pagination import PageNumberPagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20
    last_page_strings = ('the_end',)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 20
    last_page_strings = ('the_end',)