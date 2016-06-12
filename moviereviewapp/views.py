from django.shortcuts import render
from moviereviewapp.models import Rater, Movie, Review


# Create your views here.
def index_view(request):
    return render(request, "index.html")

def movie_list(request):

    context ={
       "Movies": Movie.objects.all()
    }
    return render(request, "movie.html", context)




