# For later use, we can create a custom pagination class to control the number of articles displayed per page and allow clients to specify the page size if needed. Here's how you can implement it in your `pagination.py` file:
from rest_framework.pagination import PageNumberPagination

class ArticlePagination(PageNumberPagination):
    page_size = 4 
    page_size_query_param = 'page_size'
    max_page_size = 50