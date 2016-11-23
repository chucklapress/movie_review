





from __future__ import unicode_literals
from django.db.models import Avg, Count
from django.db import migrations


def top_twenty(apps, schema_editor):
    Movie = apps.get_model('app', 'Movie')
    Review = apps.get_model('app', 'Review')
    Rating = apps.get_model('app', 'Average')

    movies = Review.objects.all()
    for movie in movies:
        average_dict = Review.objects.filter(movie=movie.id).values('rating').aggregate(average=Avg('rating'))
        average = average_dict.get('average')
        print(movie.movie_title, average)
        total_dict = Review.objects.filter(movie=movie.id).values('rating').aggregate(total=Count('rating'))
        total = total_dict.get('total')
        print(total)
        if average != None:
            Rating.objects.create(
                movie=movie,
                average=average,
                number_ratings=total
                )

    raise Exception("its good")
