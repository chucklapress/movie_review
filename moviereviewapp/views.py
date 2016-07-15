from django.shortcuts import render
from moviereviewapp.models import Rater, Movie, Review


# Create your views here.
def index_view(request):
    return render(request, "index.html")

def movie_list(request):

    context = {
       "movies": Movie.objects.all()
    }
    return render(request, "movie.html", context)

def movie_view(request):

    context = {
        "rated": Review.objects.all()
    }
    return render(request, "movie_rating.html", context)


def single_view(request,id):

    context = {
        #"movie_id": single_view(),
        "single": Movie.objects.get(id=id)
    }
    return render(request, "single_movie.html", context)

def rater_info(request):
    context = {
        "rater": Rater.objects.all(),

    }
    return render(request, "rater_information.html",context)

def movie_rating_view(request):
    context = {
        "rated": Review.objects.filter(rating=1)
    }
    return render(request, "movie_rated.html", context)
