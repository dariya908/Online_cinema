from django.http import request
from rest_framework import views, status
from .serializers import *
from rest_framework.response import Response
from .models import Movie,Category, Genre,Comment



class CategoryViews(views.APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class MovieView(views.APIView):
    def get(self,request,*args,**kwargs):
        movie=Movie.objects.all()
        serializer= MovieSerializer(movie,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def post(self,request,*args,**kwargs):
        serializer=RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class MovieDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=kwargs['movie_id'])
        except Movie.DoesNotExist:
            return Response({"data": "Movie Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get (id=kwargs['movie_id'])
        serializer = CommentHardSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.data.get('comment')
            Comment.objects.create(movie=movie,text=text,user=request.user)
            return Response({"data": "comment create successfully "}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class RatingDetailView(views.APIView):

    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get (id=kwargs['rating_id'])
        serializer = RatingDetailSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.data.get('rating')
            Rating.objects.create(movie=movie,rating=rating,user=request.user)
            return Response({"data": "rating create successfully "}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class CommentView (views.APIView):

    def post (self,request,*args,**kwargs):
        comment=Comment.object.all()
        serializer =CommentSerializer(Comment,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "OK!"}, status=status.HTTP_201_CREATED)

class RatingView (views.APIView):

    def post (self,request,*args,**kwargs):
        rating=Rating.object.all()
        serializer=RatingSerializer(Rating,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "OK!"}, status=status.HTTP_201_CREATED)



