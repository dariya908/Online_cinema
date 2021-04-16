from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['movie', 'user', 'text', 'date']

class CommentHardSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True, min_length=1)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['movie', 'user', 'rating', 'date_create']

class RatingDetailSerializer(serializers.Serializer):
    rating = serializers.CharField(required=True, min_length=1)

class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    rating = RatingSerializer (many=True)
    total_rate = serializers.SerializerMethodField()


    class Meta:
        model=Movie
        fields=['title','trailer','video','year','country','description',
                'genre','comments','rating','total_rate','avg_rate']

    def get_total_rate(self,obj):

        avg_rate=0
        totall_rate=len(obj.rating.all())
        for rating in obj.rating.all():
            avg_rate=avg_rate + rating.rating
        try:
            totall_rate = avg_rate/totall_rate
        except ZeroDivisionError:
            totall_rate=0
        obj.avg_rate=totall_rate
        return totall_rate













