from django.shortcuts import render
from inor_App.models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())  # Convert QuerySet to list of dictionaries       
    }
    return JsonResponse(data)

def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    data = {
        'name': movie.name, 
        'description': movie.description,
        'active': movie.active,
    }
    return JsonResponse(data)
