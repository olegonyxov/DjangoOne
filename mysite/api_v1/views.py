from api_v1.serializers import MovieSerializer
from first_app.models import Movie
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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

    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            queryset = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist as e:
            raise ValidationError(e)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)


    def update(self, request, pk=None):
        try:
            queryset = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist as e:
            raise ValidationError(e)
        serializer = MovieSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError(serializer.errors)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class Movies_top_tenViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Movie.objects.order_by('-user_rating')[:10]
        serializer = MovieSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.order_by('-user_rating')[:int(pk)]
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)





