from rest_framework import serializers
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        from movie.serializers.director import DirectorSerializer

        res = super().to_representation(instance)

        res["director"] = DirectorSerializer(instance.director).data
        return res
