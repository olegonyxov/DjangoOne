from rest_framework import serializers
from mysite.first_app.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'user_rating','runtime']

