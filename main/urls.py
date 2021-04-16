from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieView.as_view()),
    path('<int:movie_id>/', MovieDetailView.as_view()),
    path('rating/<int:rating_id>/', RatingDetailView.as_view())
]