from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

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
