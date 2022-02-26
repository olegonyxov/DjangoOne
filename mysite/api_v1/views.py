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

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:

        return Response(request)
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class Movies_top_tenViewSet(viewsets.ViewSet):

    def list(self,request):
        queryset= Movie.objects.order_by('-user_rating')[:10]
        serializer = MovieSerializer(queryset, many= True)
        return Response(serializer.data)



