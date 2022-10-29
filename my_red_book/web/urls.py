from django.urls import path
from .views import Red_bookView, Red_book_detailView

urlpatterns = [
    path('', Red_bookView, name='url_red_book'),
    path('red_book/<int:num>', Red_book_detailView, name='url_detail_red_book')
]
