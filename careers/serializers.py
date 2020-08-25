from rest_framework import serializers
from careers.models import Post

class PostSerializer(serializers.ModelSerializer):
    created_datetime = serializers.DateTimeField(format="%d/%m/%Y - %H:%M:%S")

    class Meta:
        model = Post
        fields = (
                'id', 'title', 'created_datetime', 'username', 'content'
                )