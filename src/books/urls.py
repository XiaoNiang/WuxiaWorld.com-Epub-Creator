from django.urls import path
from . import views

urlpatterns = [
    path('0/', views.allBooks, name='zero'),
    path('<int:bookID>/', views.results, name='non-zero'),
    path('<str:bookName>/<int:chapterID>', views.chapters, name='chapters')
]
