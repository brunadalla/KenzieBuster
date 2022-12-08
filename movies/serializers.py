from rest_framework import serializers
from users.models import User
from movies.models import Movie, RatingOptions
from users.serializers import UserSerializer

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        allow_null=True,
        choices=RatingOptions.choices,
        default=RatingOptions.G,
    )
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
    
    
