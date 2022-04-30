from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
# router.register(r'movies', views.ListMovie)
router.register(r'movies', views.MovieViewSet, basename="movies")
router.register(r'movies_top_ten', views.MoviesTopTenViewSet, basename="movies_top_ten")
# router.register(r'movie/(?P<input_title>.+)/$', views.Movies_InfoViewSet, basename='movies_info')

urlpatterns = [
    path('', include(router.urls)),
    # path('^movie/(?P<movie>.+)/$', views.Movies_InfoViewSet.as_view())
]
    # path('movies/{input_title}/', views.Movies_InfoViewSet, name='movies_info')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('movies/', views.ListMovie.as_view(), name='ListMovie'),
