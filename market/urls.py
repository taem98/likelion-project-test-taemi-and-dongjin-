from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list, name="list"),

    path('product/<int:post_id>/', views.product_detail, name="product_detail"),
    path('product/<int:post_id>/hit/', views.product_hit, name="product_hit"),
    path('product/new/', views.product_new, name="product_new"),
    path('product/edit/<int:post_id>/', views.product_edit, name="product_edit"),
    path('product/delete/<int:post_id>/',views.product_delete, name="product_delete" ),
    path('product/<int:post_id>/application/', views.product_application, name="product_application"),
    
    path('book/<int:post_id>/', views.book_detail,name="book_detail"),
    path('book/<int:post_id>/hit/', views.book_hit, name="book_hit"),
    path('book/new/', views.book_new, name="book_new"),
    path('book/edit/<int:post_id>/', views.book_edit, name="book_edit"),
    path('book/delete/<int:post_id>/', views.book_delete, name="book_delete"),

    path('room/<int:post_id>/', views.room_detail,name="room_detail"),
    path('room/<int:post_id>/hit/', views.room_hit, name="room_hit"),
    path('room/new/', views.room_new, name="room_new"),
    path('room/edit/<int:post_id>/', views.room_edit, name="room_edit"),
    path('room/delete/<int:post_id>/', views.room_delete, name="room_delete"),

    path('upload/', views.ImageUploadView, name="upload"),
    
]