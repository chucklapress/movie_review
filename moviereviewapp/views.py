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
        "rated": Review.objects.exclude(rater__review__rating__lt=4)
    }
    return render(request, "movie_rating.html", context)

def single_view(request,id):

    context = {
        #"movie_id": single_view(),
        "single": Movie.objects.get(id=id)
    }
    return render(request, "single_movie.html", context)

def rater_info(request,id):
    context = {
        "rater": Rater.objects.get(id=id)
        "location": Rater.objects.get(zipcode=str),
        "reviewed": Review.objects.get(rater__review=all)
    }
    return render(request, "rater_information.html",context)







