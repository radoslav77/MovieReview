
from django.urls import path, include
from . import views


app_name = 'main'

urlpatterns = [
        path("", views.home, name="home"),
        path("ditail/<int:id>/",views.ditail, name="ditail"),
        path("addmovies", views.add_movie, name="add_movie"),
        path("edit/<int:id>", views.edit_movies, name="edit_movies"),
        path("delete/<int:id>", views.delete_movie, name="delete_movie"),
        path("addreview/<int:id>", views.add_review, name="add_review"),
        path("editreview/<int:movie_id>/<int:review_id>", views.edit_review, name="edit_review"),
        path("deletereview/<int:movie_id>/<int:review_id>", views.delete_review, name="delete_review"),

]
