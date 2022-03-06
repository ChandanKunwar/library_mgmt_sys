from django.urls import path
from . import views

urlpatterns = [
   path("", views.homepage, name='homepage'),
   path("contact/", views.contact, name="contact"),
   path("list_books/", views.list_books, name="list_books"),
   path("add_author/",views.add_author,name="add_author"),
   path("add_books/", views.add_books,name="add_books"),
   path("edit_books/<int:id>/",views.edit_books,name="edit_books"),
   path("delete_books/<int:id>/",views.delete_books,name="delete_books"),
   path("register/",views.register,name="register"),
   path("login/",views.login,name="login"),
]
