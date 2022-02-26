from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api_v1.serializers import MovieSerializer
from first_app.models import Movie


class ListMovie(APIView):
    """
    View to list all movies in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all movies.
        """
        movies = [movie.title for movie in Movie.objects.all()]
        return Response(movies)
class MovieViewSet(viewsets.ViewSet):

    def list(self,request):
        queryset= Movie.objects.all()
        serializer = MovieSerializer(queryset, many= True)
        return Response(serializer.data)