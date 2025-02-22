from django.urls import path
from inor_App.api.views import movie_list, movie_detail


urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_detail, name='movie-detail'),
   
]
