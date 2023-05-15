from django.urls import path
# import views
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    # token url
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # This urls Book Category urls
    path('category/',views.BookCategoryView.as_view(),name = 'category-list'),
    path('category/create/',views.BookCategoryView.as_view(),name = 'category-create'),
    path('category/<str:slug>/update/',views.BookCategoryView.as_view(),name = 'category-update'),
    path('category/<str:slug>/delete/',views.BookCategoryView.as_view(),name = 'category-delete'),

    # Get a Single Book details Using Slug
    path('category/<str:slug>/view',views.SingleBookCategoryView.as_view(),name = "category-view"),

    # This urls Book details urls
    path('book/',views.BookDetailsView.as_view(),name = 'book-list'),
    path('book/<str:slug>/create/',views.BookDetailsView.as_view(),name = 'booke-create'),
    path('book/<str:slug>/update/',views.BookDetailsView.as_view(),name = 'book-update'),
    path('book/<str:slug>/delete/',views.BookDetailsView.as_view(),name = 'book-delete'),

     # Get The Book based on book details
     path('title/<str:title>',views.BookDetailsView.as_view(),name = 'book-detail'),

    # single book category
    path('category/<str:slug>/get/',views.BookCategoryView.as_view(),name = 'categoryes-get'),


 ] 