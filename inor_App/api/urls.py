from django.urls import path
#from inor_App.api.views import movie_list, movie_detail
from inor_App.api.views import MovieListAPIView, MovieDetailAPIView


urlpatterns = [
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAPIView.as_view(), name='movie-detail'),
   
]
